# TASK

## M0 — Khởi tạo

- [x] Tạo môi trường Python 3.11.
- [x] Chốt dependency.
- [x] Kiểm tra GPU/CPU/RAM.
- [x] Kiểm tra toàn bộ file text dùng UTF-8.
- [x] Hoàn thiện `.gitignore`.

## Progress Log

- 2026-07-14: Đã tạo `.venv` Python 3.11.9, thêm dependency chung và profile CUDA 12.8, triển khai notebook audit M0/M1, kiểm tra UTF-8 và kiểm tra tĩnh notebook.
- 2026-07-14: Chưa cài xong package PyTorch/CUDA do index wheel không phản hồi trong thời gian kiểm soát; chưa chạy notebook.
- 2026-07-14: Đã cài `ipykernel` vào `.venv` và đăng ký kernel `robust-gtsrb-lite` với display name `Python 3.11 (robust-gtsrb-lite)`.
- 2026-07-14: Đã cài PyTorch CUDA 12.8 thành công, cài các dependency còn lại từ `requirements.txt`, kiểm tra import/CPU-GPU bằng terminal và chốt `requirements-lock.txt`.
- 2026-07-14: M0 package-import gate: PASS.

## Next

- Người dùng chạy thủ công `notebooks/00_environment_dataset_audit.ipynb` bằng kernel `robust-gtsrb-lite`.
- Chưa đánh dấu M1 hoàn thành.
- Notebook nên chọn kernel `robust-gtsrb-lite`.

## M1 — Dataset audit

- [ ] Tải `tanganke/gtsrb`.
- [ ] Xác minh đủ 9 split.
- [ ] Xác minh mỗi split có 43 lớp.
- [ ] Kiểm tra schema, label names và image mode.
- [ ] Kiểm tra phân bố lớp train.
- [ ] Tạo train/validation stratified với seed 42.
- [ ] Không đụng vào test split khi tuning.
- [ ] Lưu `results/dataset_audit.json`.
- [ ] Lưu biểu đồ phân bố lớp.

## M2 — Baseline

- [ ] Tạo MobileNetV3-Small pretrained.
- [ ] Thay classifier thành 43 lớp.
- [ ] Huấn luyện E0.
- [ ] Lưu best checkpoint theo validation macro-F1.
- [ ] Lưu history CSV.
- [ ] Kiểm tra overfitting.
- [ ] Lưu config và environment.

## M3 — Robust augmentation

- [ ] Tạo pipeline E1.
- [ ] Giữ nguyên split và seed.
- [ ] Huấn luyện cùng protocol với E0.
- [ ] Lưu best checkpoint.
- [ ] So sánh validation metric với E0.
- [ ] Không đánh giá test nhiều lần để tuning.

## M4 — Đánh giá cuối

- [ ] Freeze model/config.
- [ ] Đánh giá E0 và E1 trên clean test.
- [ ] Đánh giá trên 7 corruption split.
- [ ] Tính mean corruption accuracy.
- [ ] Tính robustness drop.
- [ ] Tính macro precision/recall/F1.
- [ ] Lưu per-class metrics.
- [ ] Vẽ confusion matrix clean.
- [ ] Vẽ confusion matrix corruption tệ nhất.
- [ ] Chọn model cuối theo quy tắc trong `RESULTS_PROTOCOL.md`.

## M5 — ONNX benchmark

- [ ] Export model cuối sang ONNX FP32.
- [ ] Kiểm tra model bằng ONNX checker.
- [ ] So sánh output PyTorch và ONNX.
- [ ] Đo model-only latency.
- [ ] Đo end-to-end latency.
- [ ] Báo cáo P50, mean, P95 và FPS.
- [ ] Lưu model size.

## M6 — Báo cáo

- [ ] Cập nhật bảng kết quả chính.
- [ ] Viết phân tích trade-off.
- [ ] Viết limitations.
- [ ] Xác nhận không có claim “novel architecture”.
- [ ] Kiểm tra citation dataset, MobileNetV3, common corruptions và AugMix.
- [ ] Kiểm tra lại UTF-8.
