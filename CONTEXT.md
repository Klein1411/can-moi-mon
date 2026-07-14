# CONTEXT

## Trạng thái hiện tại

- Project: RobustGTSRB-Lite.
- Giai đoạn: M2_SOURCE_READY.
- Milestone hiện tại: M2.
- Notebook đã chạy: `notebooks/00_environment_dataset_audit.ipynb`.
- Kết quả thực nghiệm: M1 dataset audit PASS.

## Quyết định quan trọng

- Chỉ có hai experiment bắt buộc: E0 và E1.
- Người dùng tự chạy toàn bộ notebook.
- Codex không chạy notebook dưới bất kỳ hình thức nào.
- Comment code và notebook Markdown dùng tiếng Việt, UTF-8.
- Test set không dùng để tuning.
- Benchmark ONNX CPU batch 1 là phạm vi bắt buộc.

## Artifact hiện có

- `results/environment.json`
- `results/dataset_audit.json`
- `results/split_manifest.csv`
- `results/train_class_distribution.png`

## Việc tiếp theo

1. Người dùng chạy notebook `01_train_baseline.ipynb` thủ công.
2. Codex đọc output và artifact baseline, không chạy lại notebook.
3. Chỉ sau khi M2 đạt completion gate mới chuyển sang M3.

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

### 2026-07-14 — M1

Changed files:
- `TASK.md`
- `CONTEXT.md`

Decisions:
- Chuyển milestone hiện tại sang M2 sau khi M1 dataset audit đạt PASS.
- Giữ nguyên quy tắc không chạy lại notebook và không tải lại dataset trong lượt đánh giá này.

Results:
- Notebook `00_environment_dataset_audit.ipynb` có 10 cells, 5 code cells, không có cell chưa chạy, không có traceback.
- Artifact tồn tại và đọc được: `results/environment.json`, `results/dataset_audit.json`, `results/split_manifest.csv`, `results/train_class_distribution.png`.
- Chín split bắt buộc đều có mặt: `train`, `test`, `contrast`, `gaussian_noise`, `impulse_noise`, `jpeg_compression`, `motion_blur`, `pixelate`, `spatter`.
- Kích thước split hợp lý: `train=26640`, mỗi split còn lại `12630`.
- Mỗi split có `num_classes=43`, `invalid_label_count=0`, và ảnh đầu tiên decode được thành `RGB`.
- Bảy corruption split đều có `label_histogram_matches_test=true`.
- `split_manifest.csv` có `26640` dòng, `source_index` duy nhất, không trùng train/validation, và `22644 + 3996 = 26640`.
- Manifest được tạo bằng `train_test_split(..., random_state=SEED, stratify=train_labels)` trên tập train, không có dấu hiệu dùng test để chia validation.
- PNG `results/train_class_distribution.png` mở được và `verify()` pass.
- Notebook output có 2 cảnh báo không chặn: `TqdmWarning: IProgress not found...` và cảnh báo HF Hub không xác thực.
- UTF-8 kiểm tra qua `scripts/check_utf8.py`: PASS.

Issues:
- `dataset_audit.json` không lưu min/max label riêng; bằng chứng label nằm trong `[0, 42]` được suy ra từ `num_classes=43`, `invalid_label_count=0`, và ClassLabel 43 nhãn.

Next:
- Triển khai M2, bắt đầu từ `01_train_baseline.ipynb` sau khi người dùng sẵn sàng.

### 2026-07-14 — M2_SOURCE_READY

Changed files:
- `notebooks/01_train_baseline.ipynb`
- `TASK.md`
- `CONTEXT.md`

Decisions:
- Chỉ triển khai source E0 baseline; chưa chạy notebook, chưa training và chưa triển khai M3.
- Chỉ đọc split `train` của `tanganke/gtsrb`, sau đó tạo hai partition theo `results/split_manifest.csv`.
- Dùng MobileNetV3-Small pretrained ImageNet, fine-tune toàn bộ model, AdamW, CosineAnnealingLR, AMP CUDA và early stopping theo validation macro-F1.
- Không dùng split ngoài train/validation cho training hoặc chọn checkpoint.

Validation performed:
- Notebook JSON hợp lệ, 13 cell gồm 6 code cell.
- Tất cả code cell có `execution_count = null` và `outputs = []`.
- AST parse tất cả code cell: PASS.
- Không có lệnh papermill, nbconvert, Jupyter CLI hoặc đường dẫn tuyệt đối.
- Kiểm tra source không có test/corruption split trong training code.
- `scripts/check_utf8.py`: PASS; `git diff --check`: PASS.

Issues:
- Chưa có metric, checkpoint hoặc artifact E0 vì notebook chưa được chạy.
- Cảnh báo UTF-8 lần đầu chỉ do stdout PowerShell CP1252; chạy lại với stdout UTF-8 đã PASS.

Next:
- Người dùng tự chạy `notebooks/01_train_baseline.ipynb` từ trên xuống bằng kernel `robust-gtsrb-lite`.
- Sau khi người dùng lưu notebook và báo hoàn tất, Codex đọc output/artifact để đánh giá M2.
