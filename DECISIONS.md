# Các quyết định đã khóa

| Mục | Quyết định |
|---|---|
| Loại bài toán | Image classification |
| Dataset | `tanganke/gtsrb` |
| Số lớp | 43 |
| Backbone | MobileNetV3-Small pretrained ImageNet |
| Framework | Python 3.11, PyTorch, torchvision |
| Nguồn dữ liệu | Hugging Face Datasets |
| Input size mặc định | 128 × 128 |
| Seed | 42 |
| Validation | Stratified split từ `train`, mặc định 15% |
| Test để tuning | Không |
| Thí nghiệm bắt buộc | E0 baseline, E1 robust augmentation |
| Thí nghiệm tùy chọn | E2 AugMix + JSD |
| Metric chọn model | Validation macro-F1; accuracy dùng làm metric phụ |
| Metric robustness chính | Mean Corruption Accuracy |
| Corruption splits | 7 split có sẵn từ dataset |
| Export | ONNX FP32 |
| Benchmark chính | ONNX Runtime CPU, batch 1 |
| Notebook execution | Chỉ người dùng chạy thủ công |
| Ngôn ngữ comment/Markdown | Tiếng Việt |
| Encoding | UTF-8 |
| Tự thu thập dữ liệu | Không |
| Mục tiêu novelty | Controlled evaluation, không tuyên bố kiến trúc mới |

## Ngưỡng thành công tối thiểu

- Pipeline chạy hết trên dataset thật.
- Không dùng test set để chọn hyperparameter.
- E1 cải thiện mean corruption accuracy so với E0, hoặc có phân tích thuyết phục nếu không cải thiện.
- ONNX và PyTorch có top-1 agreement tối thiểu 99,9% trên tập kiểm tra tương đương.
- Có đầy đủ metric và artifact để tái lập kết luận.
