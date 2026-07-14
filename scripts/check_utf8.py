"""Kiểm tra các file text và notebook có đọc được bằng UTF-8 hay không."""

from __future__ import annotations

import json
import sys
from pathlib import Path

TEXT_SUFFIXES = {
    ".md",
    ".py",
    ".json",
    ".csv",
    ".txt",
    ".yaml",
    ".yml",
    ".toml",
    ".ipynb",
}

SKIP_DIRS = {
    ".git",
    ".venv",
    "venv",
    "__pycache__",
    ".ipynb_checkpoints",
    "data",
    "models",
}


def should_skip(path: Path) -> bool:
    """Bỏ qua thư mục môi trường, dữ liệu lớn và artifact nhị phân."""
    return any(part in SKIP_DIRS for part in path.parts)


def validate_file(path: Path) -> list[str]:
    """Trả về danh sách lỗi encoding hoặc cấu trúc notebook."""
    errors: list[str] = []

    try:
        content = path.read_text(encoding="utf-8")
    except UnicodeDecodeError as exc:
        return [f"{path}: không decode được bằng UTF-8: {exc}"]

    if path.suffix == ".ipynb":
        try:
            notebook = json.loads(content)
        except json.JSONDecodeError as exc:
            return [f"{path}: JSON notebook không hợp lệ: {exc}"]

        if "cells" not in notebook:
            errors.append(f"{path}: thiếu trường cells")

        for index, cell in enumerate(notebook.get("cells", [])):
            source = cell.get("source", [])
            if not isinstance(source, (list, str)):
                errors.append(f"{path}: cell {index} có source không hợp lệ")

    return errors


def main() -> int:
    """Quét repository và in kết quả kiểm tra."""
    root = Path(__file__).resolve().parents[1]
    errors: list[str] = []
    checked = 0

    for path in root.rglob("*"):
        if not path.is_file() or should_skip(path):
            continue
        if path.suffix.lower() not in TEXT_SUFFIXES and path.name not in {
            ".editorconfig",
            ".gitattributes",
            ".gitignore",
        }:
            continue

        checked += 1
        errors.extend(validate_file(path))

    if errors:
        print("UTF-8 CHECK: FAIL")
        for error in errors:
            print(f"- {error}")
        return 1

    print(f"UTF-8 CHECK: PASS — đã kiểm tra {checked} file.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
