# Đặc tả notebook

## Quy tắc chung

Mỗi notebook phải có:

1. Tiêu đề và mục tiêu.
2. Cell `CẤU HÌNH`.
3. Cell kiểm tra môi trường.
4. Các bước triển khai rõ ràng.
5. Cell lưu artifact.
6. Cell `TÓM TẮT TRẠNG THÁI`.
7. Không có output giả khi Codex tạo notebook.

Người dùng chạy thủ công từ trên xuống.

---

## `00_environment_dataset_audit.ipynb`

### Mục tiêu

- Kiểm tra môi trường.
- Tải dataset.
- Audit toàn bộ split.
- Tạo train/validation manifest.

### Artifact

- `results/environment.json`
- `results/dataset_audit.json`
- `results/split_manifest.csv`
- Biểu đồ phân bố lớp

### Không làm

- Không train model.

---

## `01_train_baseline.ipynb`

### Mục tiêu

- Đọc manifest.
- Tạo DataLoader E0.
- Train MobileNetV3-Small baseline.
- Lưu best checkpoint.

### Artifact

- `models/E0_baseline_best.pt`
- `results/E0_baseline/config.json`
- `results/E0_baseline/history.csv`
- `results/E0_baseline/validation_metrics.json`

### Điều kiện dừng

- Dataset manifest không tồn tại.
- Số lớp không phải 43.
- Loss NaN.
- Không tạo được checkpoint.

---

## `02_train_robust_aug.ipynb`

### Mục tiêu

- Dùng đúng manifest E0.
- Train cùng backbone với robust augmentation.
- Lưu checkpoint tốt nhất.

### Artifact

- `models/E1_robust_aug_best.pt`
- `results/E1_robust_aug/config.json`
- `results/E1_robust_aug/history.csv`
- `results/E1_robust_aug/validation_metrics.json`

---

## `03_evaluate_all_splits.ipynb`

### Mục tiêu

- Load E0 và E1.
- Đánh giá trên clean test và 7 corruption split.
- Tạo bảng so sánh thống nhất.
- Chọn model cuối theo protocol.

### Artifact

- `results/evaluation/split_metrics.csv`
- `results/evaluation/per_class_metrics.csv`
- `results/evaluation/predictions.csv`
- `results/evaluation/summary.json`
- Confusion matrix clean
- Confusion matrix worst corruption

### Không làm

- Không train hoặc fine-tune.

---

## `04_export_onnx_benchmark.ipynb`

### Mục tiêu

- Load model cuối.
- Export ONNX FP32.
- Kiểm tra tương đương.
- Benchmark ONNX Runtime CPU.

### Benchmark

- Batch size 1.
- Warm-up tối thiểu 30 lượt.
- Đo tối thiểu 200 lượt model-only.
- Đồng bộ và loại thời gian warm-up.
- Báo cáo mean, median/P50, P95 và FPS.
- Đo end-to-end riêng, bao gồm preprocessing.

### Artifact

- `models/robust_gtsrb_mobilenetv3.onnx`
- `results/benchmark/equivalence.json`
- `results/benchmark/latency.json`
