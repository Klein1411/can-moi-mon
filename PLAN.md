# Pipeline triển khai

## Pipeline tổng thể

```text
Hugging Face GTSRB
        │
        ▼
Dataset audit
        │
        ├── train ──► stratified train/validation
        ├── test sạch
        └── 7 corruption test splits
        │
        ▼
E0: MobileNetV3-Small baseline
        │
        ▼
E1: MobileNetV3-Small + robust augmentation
        │
        ▼
Đóng băng checkpoint và cấu hình
        │
        ▼
Đánh giá thống nhất trên 8 test splits
        │
        ▼
Chọn model theo robustness/clean trade-off
        │
        ▼
Export ONNX FP32
        │
        ▼
Kiểm tra tương đương + benchmark CPU
        │
        ▼
Bảng kết quả, biểu đồ, kết luận
```

## Luồng làm việc giữa người dùng và Codex

1. Codex đọc tài liệu và triển khai **một notebook của milestone hiện tại**.
2. Codex không chạy notebook.
3. Codex báo notebook cần chạy và artifact dự kiến.
4. Người dùng mở VS Code/Jupyter và chạy thủ công từng cell.
5. Người dùng lưu notebook có output.
6. Codex đọc output và artifact, không chạy lại.
7. Codex đánh giá, sửa lỗi nếu có và cập nhật `CONTEXT.md`.
8. Chỉ chuyển milestone khi đạt completion gate.

## Quy tắc không tuning trên test

- Chỉ dùng train/validation để:
  - Chọn learning rate.
  - Chọn epoch.
  - Chọn augmentation.
  - Chọn checkpoint.
- Chỉ chạy đánh giá test chính thức sau khi E0 và E1 đã khóa.
- Nếu phát hiện bug làm sai evaluation, được chạy lại sau khi ghi rõ lý do.

## Cấu hình mặc định

- `seed = 42`
- `image_size = 128`
- `batch_size = 64`, giảm xuống 32 nếu thiếu VRAM.
- `num_workers = 2` trên Windows; có thể dùng 0 nếu DataLoader lỗi.
- Mixed precision khi CUDA khả dụng.
- Early stopping patience: 3.
- Số epoch tối đa: 15 cho mỗi experiment.
- Optimizer mặc định: AdamW.
- Scheduler: CosineAnnealing hoặc ReduceLROnPlateau, chỉ chọn một.
- Loss: CrossEntropyLoss; cân nhắc class weights chỉ khi audit cho thấy cần thiết.

## Artifact contract

Mỗi notebook phải ghi artifact vào đường dẫn cố định, không dựa vào output màn hình.

```text
results/
├── environment.json
├── dataset_audit.json
├── split_manifest.csv
├── E0_baseline/
│   ├── config.json
│   ├── history.csv
│   └── validation_metrics.json
├── E1_robust_aug/
│   ├── config.json
│   ├── history.csv
│   └── validation_metrics.json
├── evaluation/
│   ├── split_metrics.csv
│   ├── per_class_metrics.csv
│   ├── predictions.csv
│   └── summary.json
└── benchmark/
    ├── equivalence.json
    └── latency.json

models/
├── E0_baseline_best.pt
├── E1_robust_aug_best.pt
└── robust_gtsrb_mobilenetv3.onnx
```
