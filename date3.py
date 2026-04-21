from datetime import datetime

S = 'Sep 18 2019 2:43PM'
date_obj = datetime.strptime(S, '%b %d %Y %I:%M%p')

print(f"\nChuỗi gốc: {S}")
print(f"Sau khi chuyển đổi: {date_obj}")
print(f"Kiểu dữ liệu: {type(date_obj)}")