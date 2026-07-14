# Dataset Protocol

## Dataset chính

- Hugging Face ID: `tanganke/gtsrb`
- Bài toán: phân loại ảnh biển báo.
- 43 lớp.
- Dataset card công bố:
  - `train`: 26.640 ảnh.
  - `test`: 12.630 ảnh.
  - 7 corruption split, mỗi split 12.630 ảnh.

## Chín split cần xác minh

1. `train`
2. `test`
3. `contrast`
4. `gaussian_noise`
5. `impulse_noise`
6. `jpeg_compression`
7. `motion_blur`
8. `pixelate`
9. `spatter`

Không hard-code hoàn toàn schema trước khi notebook audit in ra `dataset.features`.

## Audit bắt buộc

### 1. Kiểm tra cấu trúc

- Tên split.
- Số lượng mẫu.
- Tên cột.
- Kiểu dữ liệu ảnh.
- Kiểu dữ liệu nhãn.
- Danh sách label name.

### 2. Kiểm tra chất lượng

- Ảnh decode thành công.
- Ảnh có mode RGB hoặc được chuyển RGB nhất quán.
- Không có label ngoài `[0, 42]`.
- Mỗi split có đủ label dự kiến.
- Kích thước ảnh hợp lệ.
- Phân bố lớp train/validation.

### 3. Kiểm tra sự tương ứng của corruption split

Với mỗi corruption split:

- Số mẫu bằng clean test.
- Chuỗi label có cùng phân bố với clean test.
- Nếu dataset có ID/index tương ứng, xác minh thứ tự.
- Không giả định ảnh corruption và clean có cùng thứ tự nếu chưa kiểm tra.

### 4. Validation split

Dataset không cung cấp validation riêng trong card đang dùng, vì vậy:

- Tạo validation từ `train`.
- Stratified theo label.
- Mặc định `validation_size = 0.15`.
- Seed cố định `42`.
- Lưu index vào `results/split_manifest.csv`.
- Các experiment dùng lại manifest, không chia lại.

### 5. Nguyên tắc test set

- Không dùng `test` hoặc corruption split để tuning.
- Không chọn checkpoint theo test.
- Chỉ chạy evaluation chính thức sau khi khóa E0 và E1.
- Giữ toàn bộ metric lần chạy chính thức.

## License và citation

Dataset card hiện không nêu rõ một license chuẩn ở phần metadata. Báo cáo phải:

- Trích dẫn paper GTSRB gốc.
- Ghi nguồn Hugging Face dataset card.
- Chỉ tuyên bố sử dụng cho mục đích học thuật.
- Không tự khẳng định quyền sử dụng thương mại.
