# Security Requirements cho hàm json_search()

## SR-1: Kiểm soát truy cập dựa trên vai trò (RBAC) cho dữ liệu đầu ra
* **Yêu cầu:** Hàm `json_search()` phải tích hợp cấu hình quyền từ tệp `policy.py`. Chỉ được phép trả về các trường dữ liệu tương ứng với vai trò (`role`) của người gọi.
* **Chi tiết:** 
  * Vai trò `viewer`: Phải giấu/xóa hoàn toàn chuỗi xác thực SNMP hoặc thông tin định danh hệ thống khỏi kết quả trả về.
  * Vai trò `operator` và `admin`: Được phép tiếp cận các trường kỹ thuật theo đúng phạm vi cấu hình.

## SR-2: Xác thực tính hợp lệ của vai trò đầu vào (Input Validation)
* **Yêu cầu:** Trước khi xử lý tìm kiếm, hàm phải kiểm tra xem tham số `role` truyền vào có nằm trong danh sách hợp lệ định sẵn (`admin`, `operator`, `viewer`) hay không. Nếu không hợp lệ, phải lập tức từ chối và báo lỗi an toàn.

## SR-3: Cơ chế lọc dữ liệu mặc định an toàn (Fail-Safe Defaults)
* **Yêu cầu:** Nếu một trường dữ liệu JSON mới xuất hiện mà chưa được định nghĩa phân quyền trong `policy.py`, hệ thống phải mặc định coi trường đó là "Nhạy cảm" và chỉ cho phép `admin` xem.
