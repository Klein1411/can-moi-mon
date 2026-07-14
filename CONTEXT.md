# CONTEXT

## Trạng thái hiện tại

- Project: RobustGTSRB-Lite.
- Giai đoạn: chuẩn bị triển khai.
- Milestone hiện tại: M0.
- Notebook đã chạy: chưa có.
- Kết quả thực nghiệm: chưa có.

## Quyết định quan trọng

- Chỉ có hai experiment bắt buộc: E0 và E1.
- Người dùng tự chạy toàn bộ notebook.
- Codex không chạy notebook dưới bất kỳ hình thức nào.
- Comment code và notebook Markdown dùng tiếng Việt, UTF-8.
- Test set không dùng để tuning.
- Benchmark ONNX CPU batch 1 là phạm vi bắt buộc.

## Artifact hiện có

- Chưa có artifact thực nghiệm.

## Việc tiếp theo

1. Codex triển khai M0 và notebook `00_environment_dataset_audit.ipynb`.
2. Người dùng chạy notebook thủ công.
3. Codex đọc output và cập nhật file này.

## Context delta template

Sau mỗi milestone, thêm:

```text
### YYYY-MM-DD — Mx

Changed files:
- ...

Decisions:
- ...

Results:
- ...

Issues:
- ...

Next:
- ...
```

### 2026-07-14 — M0

Changed files:
- `.gitignore`
- `requirements.txt`
- `requirements-cu128.txt`
- `requirements-lock.txt`
- `notebooks/00_environment_dataset_audit.ipynb`
- `TASK.md`
- `CONTEXT.md`

Decisions:
- Dùng Python 3.11.9 trong `.venv`.
- Tách dependency chung và profile PyTorch CUDA 12.8.
- Notebook 00 ghi environment, audit chín split và manifest stratified seed 42.
- Đăng ký kernel Jupyter `robust-gtsrb-lite` trỏ vào `.venv` với display name `Python 3.11 (robust-gtsrb-lite)`.

Results:
- Kiểm tra UTF-8 và JSON notebook: PASS.
- Máy có Windows, Python hệ thống 3.12.10, Python 3.11.9 trong venv, GPU NVIDIA GeForce RTX 3050 Laptop GPU 4 GB, driver 595.95.
- Chưa chạy notebook và chưa có artifact thực nghiệm.
- `ipykernel` đã cài trong `.venv` và kernel đã xuất hiện trong `jupyter kernelspec list`.
- PyTorch/torchvision/các dependency còn lại đã cài xong trong `.venv`.
- Kiểm tra import bằng terminal: PASS.
- `torch.cuda.is_available()` = `True`, `torch.version.cuda` = `12.8`, GPU = `NVIDIA GeForce RTX 3050 Laptop GPU`.
- Tensor CUDA nhỏ tính toán thành công: `torch.tensor([1.0, 2.0], device='cuda') * 2` cho kết quả `6.0`.
- M0 package-import gate: PASS.

Issues:
- Lần cài trước không sinh traceback pip rõ ràng; tiến trình dừng ở bước tải wheel lớn `torch-2.11.0+cu128-cp311-cp311-win_amd64.whl` trước khi chạy lại thành công.

Next:
- Người dùng chạy thủ công `00_environment_dataset_audit.ipynb` bằng kernel `robust-gtsrb-lite`.
- M1 vẫn chưa bắt đầu.
