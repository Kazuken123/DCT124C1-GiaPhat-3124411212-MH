# GIÁO ÁN TỔNG HỢP KIẾN THỨC & TÀI LIỆU DẠY HỌC - LAB 01 PYTORCH
Dành cho: Sinh viên Gia Phát (MSSV: 3124411212 - Lớp DCT124C1)
Môn học: Máy học (Machine Learning)

---

## 1. Bản chất các kiến thức cốt lõi đã áp dụng

### Chuyên đề 1: Tensor căn bản & Các hàm sinh dữ liệu (Bài 1 - 3)
- **Tensor là gì?** Tensor là mảng đa chiều tương tự NumPy ndarray nhưng được tối ưu để tính toán song song trên GPU và hỗ trợ tự động tính đạo hàm (autograd).
- **Thuộc tính cơ bản:**
  - `shape` / `size()`: Kích thước các chiều của Tensor.
  - `ndim`: Số chiều (rank của Tensor).
  - `dtype`: Kiểu dữ liệu phần tử (ví dụ: `torch.float32`, `torch.int32`).
- **Phân biệt sinh ngẫu nhiên:**
  - `torch.rand()`: Phân phối đều (Uniform) trong khoảng [0, 1).
  - `torch.randn()`: Phân phối chuẩn chuẩn hóa (Normal) với trung bình = 0, độ lệch chuẩn = 1.
  - `torch.full((m, n), val)`: Tạo ma trận m x n với giá trị cố định `val`.

### Chuyên đề 2: Kỹ thuật Slicing, Indexing & Reshape (Bài 4 - 5)
- **Slicing đa chiều:** Tương tự Python/NumPy. `a[:, :, -2:]` nghĩa là giữ nguyên chiều 0 và 1, lấy 2 phần tử cuối ở chiều thứ 3.
- **Biến đổi hình dạng:**
  - `ravel()`: Trải phẳng Tensor thành 1 chiều (flatten).
  - `reshape(d1, d2, ...)`: Thay đổi kích thước nhưng BẢO TOÀN tổng số phần tử (`numel()`). Ví dụ: 3x4 = 12 phần tử có thể reshape thành 2x6 hoặc 3x2x2.

### Chuyên đề 3: Phép toán đại số ma trận & Thống kê (Bài 6 - 7)
- **Phân biệt `*` và `@`:**
  - `a * b`: Hadamard product (nhân từng phần tử tương ứng, 2 ma trận cùng kích thước).
  - `a @ b.T`: Matrix multiplication (nhân ma trận đại số tuyến tính: (2x3) @ (3x2) -> (2x2)).
- **Ý nghĩa của trục `dim` trong tính toán thống kê:**
  - `dim=0`: Thu gọn dọc theo hàng -> tính toán cho từng cột (kết quả có số chiều = số cột).
  - `dim=1`: Thu gọn ngang qua các cột -> tính toán cho từng hàng (kết quả có số chiều = số hàng).

### Chuyên đề 4: Autograd & Tối ưu hóa Gradient Descent (Bài 8 - 11)
- **Autograd:** Đặt `requires_grad=True` trên tensor đầu vào để PyTorch theo dõi đồ thị tính toán (computational graph).
- **Quy trình 3 bước vàng khi huấn luyện Deep Learning / Machine Learning:**
  1. `optimizer.zero_grad()`: Xóa sạch gradient tích lũy từ bước trước về 0.
  2. `loss.backward()`: Lan truyền ngược (Backpropagation) để tự động tính đạo hàm của hàm mất mát theo từng tham số cần tối ưu.
  3. `optimizer.step()`: Cập nhật trọng số theo hướng giảm của đạo hàm: w_new = w_old - lr * gradient.
- **Giải hệ phương trình bằng tối ưu hóa (Bài 10):**
  - Biến bài toán giải phương trình thành bài toán tìm cực tiểu của tổng bình phương sai số: loss = sum((y_i - target_i)^2). Khi loss xấp xỉ 0, các giá trị đạt nghiệm.

---

## 2. Kỹ năng Git & Quản lý Repository
- `git clone <url>`: Tải dự án về máy tính.
- `git status`: Kiểm tra trạng thái các file đã thay đổi.
- `git add .`: Đưa tất cả file thay đổi vào staging area.
- `git commit -m "nội dung"`: Đóng gói một phiên bản cập nhật.
- `git push origin main`: Đẩy các commit lên GitHub.
