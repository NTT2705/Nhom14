# Phân tích Bối cảnh & Threat Model cho hàm json_search()

## 1. Phân tích bối cảnh sử dụng (Context Analysis)
* **Mục đích:** Hàm `json_search()` đóng vai trò là một bộ lọc trung gian, nhận yêu cầu tra cứu từ người dùng, tìm kiếm trên cấu trúc JSON từ API giám sát hạ tầng (mô phỏng trong `test_data.py`), và trả về kết quả.
* **Đối tượng sử dụng và phạm vi dữ liệu:**
  * **Admin:** Tra cứu toàn bộ dữ liệu hệ thống mạng để cấu hình và xử lý sự cố (bao gồm cả chuỗi xác thực SNMP nhạy cảm).
  * **Operator:** Tra cứu thông tin kỹ thuật chuyên sâu (IP, Port, trạng thái kết nối) để vận hành hàng ngày, không được xem mật mã/chuỗi xác thực.
  * **Viewer:** Chỉ được tra cứu thông tin cơ bản không nhạy cảm (Tên hiển thị thiết bị, uptime) để xem báo cáo tổng quan.

## 2. Đường biên tin cậy (Trust Boundary)
* Ranh giới giữa đầu vào từ người dùng (vai trò/role) và dữ liệu hệ thống thô từ API. Hàm bắt buộc phải kiểm tra quyền từ `policy.py` trước khi trả về kết quả tại biên này.

## 3. Phân tích mối đe dọa theo mô hình STRIDE
* **T1: Information Disclosure (Rò rỉ thông tin):** Người dùng có vai trò thấp (`viewer`) cố tình hoặc vô tình gọi hàm `json_search()` để lấy ra các thông tin nhạy cảm của hệ thống mạng (chuỗi xác thực SNMP, cấu hình lõi).
* **T2: Elevation of Privilege (Leo thang đặc quyền):** Kẻ tấn công thao túng tham số `role` truyền vào hàm (giả mạo từ `viewer` thành `admin`) để chiếm quyền truy cập trái phép vào toàn bộ dữ liệu.
