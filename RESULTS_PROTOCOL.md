# Quy trình đọc và đánh giá kết quả

## Sau mỗi notebook

Codex chỉ được đánh giá sau khi người dùng đã:

1. Chạy notebook thủ công.
2. Lưu notebook có output.
3. Thông báo notebook đã chạy xong.

## Checklist đọc output

- Cell cuối có trạng thái thành công hay không.
- Có traceback không.
- Artifact có tồn tại không.
- JSON/CSV có đọc được không.
- Metric có NaN/Inf không.
- Số mẫu đánh giá có đúng không.
- Số lớp có đúng 43 không.
- Checkpoint được chọn theo validation macro-F1 không.
- Test split có bị dùng trong training/tuning không.

## Chẩn đoán training

### Underfitting

- Train và validation metric cùng thấp.
- Loss giảm chậm hoặc không giảm.
- Có thể do backbone bị freeze quá lâu, LR không phù hợp hoặc input quá nhỏ.

### Overfitting

- Train metric tăng nhưng validation metric giảm.
- Khoảng cách train/validation lớn.
- Cần early stopping hoặc augmentation/regularization hợp lý.

### Robust augmentation quá mạnh

- Clean accuracy giảm rõ.
- Validation macro-F1 giảm.
- Ảnh augmentation khó nhận dạng bằng mắt.
- Robustness không tăng tương ứng.

## Bảng kết quả chính

| Model | Clean Acc | Clean Macro-F1 | Mean Corruption Acc | Robustness Drop | Size MB | ONNX P50 ms | ONNX P95 ms |
|---|---:|---:|---:|---:|---:|---:|---:|
| E0 | | | | | | | |
| E1 | | | | | | | |

## Kết luận được phép

- E1 cải thiện hoặc không cải thiện robustness theo metric.
- Có trade-off giữa clean accuracy và corruption accuracy.
- Model ONNX có hoặc không tương đương với PyTorch.
- Pipeline có độ trễ đo được trên phần cứng cụ thể.

## Kết luận không được phép

- “Model hoạt động an toàn trên xe thật.”
- “Model tổng quát cho biển báo Việt Nam.”
- “Kiến trúc mới.”
- “SOTA” nếu không benchmark theo cùng protocol với công trình khác.
