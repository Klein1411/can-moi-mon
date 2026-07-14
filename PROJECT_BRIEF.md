# Project Brief

## Tên đề tài

**RobustGTSRB-Lite: Đánh giá và cải thiện độ bền của MobileNetV3-Small trong nhận diện biển báo giao thông**

## Bài toán

Mô hình phân loại ảnh có thể đạt accuracy cao trên ảnh sạch nhưng giảm mạnh khi ảnh bị nhiễu, mờ, nén hoặc thay đổi tương phản. Project đánh giá liệu augmentation hướng tới robustness có cải thiện hiệu năng trên các corruption test set mà vẫn giữ được clean accuracy và hiệu quả suy luận hay không.

## Câu hỏi nghiên cứu

**RQ1.** MobileNetV3-Small đạt hiệu năng như thế nào trên GTSRB clean test và bảy corruption test set?

**RQ2.** Robust augmentation cải thiện mean corruption accuracy bao nhiêu so với baseline?

**RQ3.** Robust augmentation có làm giảm clean accuracy đáng kể không?

**RQ4.** Model tốt nhất có phù hợp cho suy luận nhẹ khi xét model size và ONNX CPU latency không?

## Giả thuyết

- `H1`: Robust augmentation làm tăng mean corruption accuracy.
- `H2`: Clean accuracy giảm không quá 1,5 điểm phần trăm so với baseline.
- `H3`: MobileNetV3-Small ONNX giữ sai khác dự đoán rất nhỏ so với PyTorch và có kích thước phù hợp cho triển khai nhẹ.

## Deliverables

1. Năm notebook được người dùng chạy thủ công.
2. Hai checkpoint bắt buộc: baseline và robust augmentation.
3. Bảng metric trên tám test split.
4. Confusion matrix trên clean split và corruption tệ nhất.
5. File ONNX của model được chọn.
6. Benchmark latency/FPS CPU.
7. Báo cáo phân tích trade-off.
