# Prompt dùng với Codex 5.4 mini

## Prompt khởi động project

```text
Đọc AGENTS.md, DECISIONS.md, CONTEXT.md, TASK.md, PLAN.md, MILESTONES.md và NOTEBOOKS.md.

Chỉ triển khai milestone hiện tại được ghi trong CONTEXT.md. Không chạy bất kỳ file ipynb nào và không dùng công cụ chạy notebook gián tiếp. Người dùng sẽ tự chạy từng notebook, lưu output, rồi yêu cầu bạn đọc và đánh giá.

Mọi Markdown trong notebook và mọi comment code phải viết bằng tiếng Việt có dấu. Mọi file text và notebook phải dùng UTF-8. Dùng tên biến/hàm tiếng Anh rõ nghĩa. Không tạo số liệu hoặc output giả.

Khi hoàn tất, trả về:
1. File đã tạo/sửa.
2. Notebook người dùng cần chạy.
3. Thứ tự chạy.
4. Artifact dự kiến.
5. Điều kiện dừng nếu gặp lỗi.
6. Context delta ngắn.
```

## Prompt sau khi người dùng chạy notebook

```text
Tôi đã chạy thủ công và lưu notebook <TÊN_NOTEBOOK>. Hãy đọc notebook cùng các artifact được tạo ra. Không chạy lại notebook hoặc training.

Kiểm tra lỗi, tính đầy đủ của artifact, metric, dấu hiệu leakage/overfitting/NaN và completion gate của milestone. Sau đó:
1. Kết luận PASS, PASS_WITH_WARNINGS hoặc FAIL.
2. Nêu bằng chứng từ output/artifact.
3. Cập nhật CONTEXT.md và TASK.md.
4. Chỉ đề xuất sửa notebook nếu thật sự cần.
5. Không chuyển milestone nếu chưa đạt gate.
```

## Prompt triển khai notebook kế tiếp

```text
Dựa trên CONTEXT.md đã cập nhật, triển khai đúng notebook của milestone kế tiếp theo NOTEBOOKS.md. Không chạy notebook. Giữ nguyên các quyết định trong DECISIONS.md và tái sử dụng artifact hợp lệ đã có.
```
