# AGENTS.md — Chỉ dẫn bắt buộc cho Codex

## 1. Ưu tiên chỉ dẫn

Khi làm việc trong repository này, phải đọc theo thứ tự:

1. `AGENTS.md`
2. `DECISIONS.md`
3. `CONTEXT.md`
4. `TASK.md`
5. File đặc tả liên quan đến milestone hiện tại

Không tự thay đổi phạm vi đã khóa nếu người dùng chưa yêu cầu.

## 2. Cấm tự động chạy notebook

Codex **không được thực thi bất kỳ notebook nào**.

Các hành vi bị cấm:

- Chạy cell bằng Jupyter.
- Chạy `jupyter notebook`, `jupyter lab` hoặc `jupyter execute`.
- Dùng `jupyter nbconvert --execute`.
- Dùng `papermill`.
- Dùng Python để import và thực thi cell notebook.
- Chạy notebook gián tiếp thông qua test hoặc script.
- Tự động xóa output của notebook mà người dùng đã chạy.

Codex được phép:

- Tạo notebook.
- Chỉnh sửa source của cell.
- Đọc notebook đã được người dùng chạy.
- Đọc output, log và artifact đã lưu.
- Phân tích kết quả sau khi người dùng xác nhận đã chạy xong.

Sau khi chỉnh notebook, phải đưa ra:

1. Danh sách file đã đổi.
2. Notebook người dùng cần chạy.
3. Thứ tự cell cần chạy.
4. Output/artifact dự kiến.
5. Điều kiện dừng nếu có lỗi.

## 3. Ngôn ngữ và encoding

- Markdown trong notebook: tiếng Việt.
- Comment trong code: tiếng Việt.
- Tên biến, hàm và class: tiếng Anh rõ nghĩa.
- File text phải dùng UTF-8.
- Notebook JSON phải lưu bằng UTF-8 và không chứa output giả.
- Không dùng comment tiếng Việt bị mất dấu.
- Không thay thế ký tự tiếng Việt bằng chuỗi escape không cần thiết.

Sau mỗi lần tạo hoặc sửa file text/notebook:

- Kiểm tra file decode được bằng UTF-8.
- Chạy `python scripts/check_utf8.py` chỉ khi người dùng yêu cầu chạy script hoặc đang làm việc ngoài notebook.
- Không dùng script UTF-8 để chạy notebook.

## 4. Quy tắc triển khai

- Chỉ thực hiện milestone hiện tại.
- Không mở rộng sang tính năng tùy chọn khi phần bắt buộc chưa hoàn tất.
- Ưu tiên code đơn giản, tái lập được và có kiểm tra lỗi.
- Dùng đường dẫn tương đối; không hard-code đường dẫn máy cá nhân.
- Tất cả seed mặc định là `42`.
- Mọi cấu hình quan trọng phải tập trung trong cell `CẤU HÌNH`.
- Không tải lại dataset hoặc train lại model nếu artifact hợp lệ đã tồn tại, trừ khi người dùng yêu cầu.
- Không ghi model hoặc dataset lớn vào Git.
- Không sửa số liệu bằng tay.
- Không điền kết quả giả vào CSV, Markdown hoặc notebook.

## 5. Quy tắc đánh giá sau khi người dùng chạy notebook

Khi người dùng báo đã chạy xong:

1. Đọc notebook và artifact đầu ra, không chạy lại.
2. Kiểm tra output cuối cùng có trạng thái thành công.
3. Kiểm tra file kết quả thực sự tồn tại.
4. Đối chiếu metric với tiêu chí milestone.
5. Tìm dấu hiệu lỗi, leakage, NaN, overfitting hoặc sai split.
6. Ghi kết luận có căn cứ vào `CONTEXT.md`.
7. Cập nhật checkbox trong `TASK.md`.
8. Không đánh dấu milestone hoàn thành nếu thiếu artifact bắt buộc.

## 6. Quy tắc Git

- Commit nhỏ, theo milestone.
- Không commit dataset cache, checkpoint tạm hoặc environment cục bộ.
- Không force push.
- Không xóa file kết quả của người dùng nếu chưa được yêu cầu.
- Khi thay notebook đã có output, giữ output trừ khi việc sửa source làm output cũ trở nên sai; trong trường hợp đó phải báo rõ trước khi xóa.
