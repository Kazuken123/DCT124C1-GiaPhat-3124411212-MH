# QUY TẮC LÀM VIỆC DỰ ÁN (PROJECT RULES)

Agent PHẢI tuân thủ các quy định sau khi làm việc trên repository này:

## 1. Thông tin sinh viên
- **Họ và tên:** Gia Phát
- **MSSV:** 3124411212
- **Lớp:** DCT124C1
- **Môn học:** Machine Learning (Máy học)

---

## 2. Cấu trúc thư mục bài tập theo tuần
Mỗi tuần học mới, tạo một thư mục riêng dạng `TuanXX` (ví dụ: `Tuan01`, `Tuan02`,...).  
Bên trong mỗi thư mục tuần phải chuẩn bị đầy đủ các tệp sau:
1. `labXX.ipynb`: File Jupyter Notebook giải hoàn chỉnh tất cả các bài thực hành có kèm Markdown giải thích.
2. `labXX_LuyenTap.ipynb`: File thực hành tự luyện (dạng skeleton code / TODO điền khuyết) để sinh viên tự tay gõ code rèn luyện kỹ năng.
3. `labXX_GiaPhat_3124411212.docx`: File báo cáo Word chuẩn mực (có trang bìa thông tin sinh viên, code định dạng khung, kết quả chạy thực tế và trả lời câu hỏi trực diện).
4. `labXX_GiaPhat_3124411212.zip`: File nén chứa `.ipynb` và `.docx` sẵn sàng để nộp lên hệ thống.
5. `Giao_An_Hoc_Tap_PyTorch_LabXX.md`: Giáo án tóm tắt lý thuyết cốt lõi, bản chất toán học và hướng dẫn học tập.

---

## 3. Quy trình Cập nhật & Git
- **Quy tắc Commit Message:** Bắt buộc tuân thủ chuẩn định dạng: `Tuan??/Bai??/Làm cái gì?` (Ví dụ: `Tuan03/Bai01/Them cac attached files du an du doan gia nha House Prices`).
- **README.md:** Mỗi khi hoàn thành hoặc cập nhật bài tập mới, luôn tự động ghi nhận vào mục **Nhật ký cập nhật** trong `README.md` theo định dạng: `[YYYY-MM-DD] - <Nội dung cập nhật>`.
- **Git:** Tự động thực hiện quy trình đồng bộ GitHub: `git status` -> `git add .` -> `git commit -m "Tuan??/Bai??/Làm cái gì?"` -> `git push origin main`.

---

## 4. Phương pháp Hỗ trợ & Giảng dạy (Pair Programming)
- Khi sinh viên yêu cầu tự học / tự code: Không đưa code giải sẵn ngay lập tức, mà đóng vai trò là Mentor (người hướng dẫn):
  - Phân tích yêu cầu và bản chất toán học/logic trước.
  - Cung cấp khung sườn (skeleton code) để sinh viên tự gõ vào.
  - Hướng dẫn đọc lỗi (debug), giải thích nguyên nhân lỗi và cách khắc phục.
  - Khuyến khích sinh viên tự tay thực thi các lệnh Terminal / Git.
