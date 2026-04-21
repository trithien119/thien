from datetime import datetime
import math

now = datetime.now()

print("--- THÔNG TIN HIỆN TẠI ---")
print(f"Năm hiện tại: {now.year}")
print(f"Tháng hiện tại bằng chữ: {now.strftime('%B')}")
print(f"Tuần hiện tại là tuần thứ mấy trong năm: {now.strftime('%U')}")
first_day = now.replace(day=1)
week_of_month = math.ceil((now.day + first_day.weekday()) / 7)
print(f"Tuần hiện tại là tuần thứ mấy trong tháng: {week_of_month}")
print(f"Ngày hiện tại là ngày thứ mấy trong năm: {now.strftime('%j')}")
print(f"Ngày dương lịch hiện tại là ngày: {now.day}")
print(f"Thứ của ngày hiện tại: {now.strftime('%A')}")
print(f"Giờ phút giây hiện tại: {now.strftime('%H:%M:%S')}")