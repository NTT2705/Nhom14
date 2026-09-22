# policy.py
# Quy định vai trò (role) nào được phép đọc giá trị của một trường (key)
# cụ thể trong dữ liệu JSON trả về bởi json_search().
#
# Sinh viên dùng bảng này để viết security test ở Yêu cầu 6: gọi
# json_search(key, data, role=...) với một role KHÔNG nằm trong danh sách
# cho phép của key đó, và kỳ vọng kết quả trả về là rỗng.

POLICY = {
    "apiKey": ["admin"],
    "managementIpAddress": ["admin", "operator"],
    "issueSummary": ["admin", "operator", "viewer"],
}
