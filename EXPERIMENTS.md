# Experiment Design

## Biến kiểm soát chung

Giữa E0 và E1 phải giữ nguyên:

- Train/validation indices.
- Seed.
- Backbone.
- Input size.
- Optimizer.
- Scheduler.
- Epoch limit.
- Early stopping.
- Batch size nếu phần cứng cho phép.
- Metric chọn checkpoint.
- Pretrained weights.
- Evaluation code.

## E0 — Baseline

### Augmentation train

- Resize về kích thước đầu vào.
- Random rotation nhỏ.
- Random affine/translation nhẹ.
- Color jitter nhẹ.
- Normalize theo pretrained weights.

Không dùng corruption mạnh trong baseline.

### Validation/test

- Resize.
- Chuyển tensor.
- Normalize.
- Không augmentation ngẫu nhiên.

## E1 — Robust augmentation

Cấu hình bắt buộc phải giữ biển báo còn nhận dạng được.

Gợi ý pipeline:

- RandomApply Gaussian blur.
- RandomAdjustSharpness.
- RandomAutocontrast hoặc ColorJitter mạnh hơn baseline.
- Gaussian noise custom.
- JPEG compression augmentation custom.
- Random affine nhẹ.
- Có thể dùng `torchvision.transforms.AugMix` như một transform, nhưng phải mô tả đúng là **AugMix transform** nếu không triển khai consistency loss.

Không áp dụng corruption quá mạnh đồng thời với xác suất cao.

## E2 — AugMix + JSD, tùy chọn

Chỉ làm sau khi E0, E1, M4 và M5 hoàn thành.

Yêu cầu:

- Một ảnh gốc và hai phiên bản AugMix.
- Cross-entropy trên ảnh gốc.
- Jensen–Shannon consistency loss giữa ba dự đoán.
- Ghi rõ đây mới là reproduction gần với phương pháp AugMix đầy đủ.

## Metric

### Classification

- Accuracy.
- Macro precision.
- Macro recall.
- Macro-F1.
- Per-class precision/recall/F1.

### Robustness

```text
Mean Corruption Accuracy = trung bình accuracy của 7 corruption splits

Robustness Drop = Clean Accuracy - Mean Corruption Accuracy
```

Có thể báo cáo Relative Robustness Drop như metric phụ.

### Efficiency

- Số tham số.
- File size.
- Mean latency.
- P50 latency.
- P95 latency.
- FPS = 1000 / mean_latency_ms.

## Quy tắc chọn model cuối

1. Loại model nếu clean accuracy giảm hơn 1,5 điểm phần trăm so với baseline, trừ khi robustness tăng rất lớn và báo cáo giải thích rõ.
2. Ưu tiên model có mean corruption accuracy cao hơn.
3. Nếu chênh lệch robustness rất nhỏ, chọn model đơn giản hơn.
4. Không chọn model bằng test metric trước khi cả hai model đã được khóa.
