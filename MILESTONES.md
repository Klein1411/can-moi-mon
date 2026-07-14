# Milestone và lịch 7 ngày

## Tổng quan

| Ngày | Milestone | Output bắt buộc |
|---:|---|---|
| 1 | M0 + M1 | Environment và dataset audit |
| 2 | M2 | Baseline checkpoint + history |
| 3 | M3 | Robust checkpoint + history |
| 4 | M4 phần 1 | Đánh giá 8 split |
| 5 | M4 phần 2 | Phân tích, confusion matrix, chọn model |
| 6 | M5 | ONNX + benchmark |
| 7 | M6 | Báo cáo, slide, kiểm tra tái lập |

## M0 — Repository và môi trường

### Completion gate

- Python và package import thành công.
- CUDA được ghi nhận nếu có.
- Không có file text lỗi UTF-8.
- Notebook chưa được chạy tự động.

## M1 — Dataset audit

### Completion gate

- Có đúng các split cần thiết.
- Label mapping nhất quán.
- Train/validation manifest cố định.
- Không dùng test để tuning.
- Có `dataset_audit.json`.

### Dừng project để sửa nếu

- Thiếu split.
- Label mapping khác nhau giữa clean và corrupted split.
- Ảnh không decode được ở tỷ lệ đáng kể.
- Validation split không tái lập.

## M2 — Baseline

### Completion gate

- Training kết thúc không NaN.
- Có best checkpoint.
- Có history và validation metric.
- Accuracy/macro-F1 cao hơn random đáng kể.
- Không có lỗi số lớp hoặc preprocessing.

## M3 — Robust augmentation

### Completion gate

- Dùng đúng cùng split với baseline.
- Chỉ khác augmentation hoặc loss đã khai báo.
- Có best checkpoint và history.
- Không dùng test split để chọn tham số.

## M4 — Đánh giá cuối

### Completion gate

- Có metric của E0 và E1 trên 8 split.
- Có mean corruption accuracy.
- Có robustness drop.
- Có confusion matrix clean và worst corruption.
- Có kết luận model nào tốt hơn và vì sao.

## M5 — ONNX

### Completion gate

- ONNX checker pass.
- Top-1 agreement đạt ngưỡng.
- Có latency model-only và end-to-end.
- Có model size.

## M6 — Hoàn thiện

### Completion gate

- Báo cáo chỉ sử dụng số liệu từ artifact.
- Hạn chế được nêu rõ.
- Citation đầy đủ.
- Không có claim vượt quá thí nghiệm.
- Toàn repository pass kiểm tra UTF-8.
