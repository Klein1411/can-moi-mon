# RobustGTSRB-Lite

## 1. Mục tiêu

Xây dựng và đánh giá một mô hình **MobileNetV3-Small** nhận diện 43 lớp biển báo giao thông trên GTSRB, tập trung vào ba tiêu chí:

1. Độ chính xác trên ảnh sạch.
2. Độ bền trước bảy dạng suy giảm ảnh.
3. Hiệu quả triển khai thông qua kích thước mô hình và độ trễ ONNX Runtime.

Đây là project **image classification**, không phải object detection.

## 2. Phạm vi đã khóa

### Bắt buộc

- Dataset: `tanganke/gtsrb` từ Hugging Face.
- Model: MobileNetV3-Small pretrained ImageNet.
- Hai thí nghiệm:
  - `E0_baseline`: augmentation cơ bản.
  - `E1_robust_aug`: augmentation hướng tới robustness.
- Đánh giá trên:
  - `test`
  - `contrast`
  - `gaussian_noise`
  - `impulse_noise`
  - `jpeg_compression`
  - `motion_blur`
  - `pixelate`
  - `spatter`
- Export model tốt nhất sang ONNX.
- Benchmark ONNX Runtime CPU với batch size 1.
- Báo cáo accuracy, macro-F1, mean corruption accuracy, robustness drop, model size và latency.

### Tùy chọn, chỉ làm khi hoàn thành toàn bộ phần bắt buộc

- `E2_augmix_jsd`: AugMix đầy đủ với consistency loss.
- Calibration/ECE.
- Quantization INT8.
- Demo giao diện.

### Không làm

- Lane detection.
- Traffic-sign object detection.
- TTS, ASR, GPS, RAG hoặc VLM.
- Tự thu thập hoặc tự gán nhãn dữ liệu.
- Tự động thực thi notebook.
- TFLite/TensorRT trong phạm vi bắt buộc.

## 3. Quy tắc notebook

- Người dùng tự mở và chạy từng notebook.
- Codex chỉ tạo hoặc chỉnh sửa notebook; **không được chạy notebook**.
- Không dùng `papermill`, `nbconvert --execute`, Jupyter CLI hoặc script để chạy notebook.
- Sau khi người dùng chạy và lưu notebook, Codex mới đọc output/artifact để đánh giá.
- Notebook phải được chạy theo đúng thứ tự trong `NOTEBOOKS.md`.

## 4. Tài liệu điều phối

| File | Vai trò |
|---|---|
| `AGENTS.md` | Quy tắc bắt buộc dành cho Codex |
| `PROJECT_BRIEF.md` | Mục tiêu, câu hỏi nghiên cứu và phạm vi |
| `DECISIONS.md` | Các quyết định đã khóa |
| `TASK.md` | Danh sách công việc |
| `PLAN.md` | Pipeline và thứ tự triển khai |
| `MILESTONES.md` | Milestone, điều kiện hoàn thành và lịch 7 ngày |
| `DATASET_PROTOCOL.md` | Quy trình audit và sử dụng dataset |
| `EXPERIMENTS.md` | Cấu hình thí nghiệm |
| `NOTEBOOKS.md` | Đặc tả từng notebook |
| `RESULTS_PROTOCOL.md` | Cách đọc và kết luận từ kết quả |
| `CONTEXT.md` | Trạng thái project theo từng lần cập nhật |
| `CODEX_PROMPT.md` | Prompt ngắn để giao từng milestone cho Codex |
| `REFERENCES.md` | Tài liệu tham khảo cốt lõi |

## 5. Cấu trúc dự kiến

```text
robust-gtsrb-lite/
├── AGENTS.md
├── README.md
├── PROJECT_BRIEF.md
├── DECISIONS.md
├── TASK.md
├── PLAN.md
├── MILESTONES.md
├── DATASET_PROTOCOL.md
├── EXPERIMENTS.md
├── NOTEBOOKS.md
├── RESULTS_PROTOCOL.md
├── CONTEXT.md
├── CODEX_PROMPT.md
├── REFERENCES.md
├── .editorconfig
├── .gitattributes
├── data/
├── models/
├── notebooks/
│   ├── 00_environment_dataset_audit.ipynb
│   ├── 01_train_baseline.ipynb
│   ├── 02_train_robust_aug.ipynb
│   ├── 03_evaluate_all_splits.ipynb
│   └── 04_export_onnx_benchmark.ipynb
├── results/
└── scripts/
    └── check_utf8.py
```

## 6. Nguyên tắc kết luận

Không tuyên bố tạo kiến trúc mới. Đóng góp là một đánh giá có kiểm soát về trade-off giữa:

- Clean accuracy.
- Corruption robustness.
- Kích thước mô hình.
- Độ trễ suy luận.
