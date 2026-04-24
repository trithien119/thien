from datetime import datetime, date, timedelta
import math

# i. Viết chương trình in ra các thông tin thời gian hiện tại
print("--- CÂU I: THÔNG TIN HIỆN TẠI ---")
bay_gio = datetime.now()

print(f"Năm hiện tại: {bay_gio.year}")
print(f"Tháng hiện tại bằng chữ: {bay_gio.strftime('%B')}")
print(f"Tuần hiện tại là tuần thứ mấy trong năm: {bay_gio.strftime('%U')}")
ngay_dau_thang = bay_gio.replace(day=1)
tuan_trong_thang = math.ceil((bay_gio.day + ngay_dau_thang.weekday()) / 7)
print(f"Tuần hiện tại là tuần thứ mấy trong tháng: {tuan_trong_thang}")
print(f"Ngày hiện tại là ngày thứ mấy trong năm: {bay_gio.strftime('%j')}")
print(f"Ngày dương lịch hiện tại là ngày: {bay_gio.day}")
print(f"Thứ của ngày hiện tại: {bay_gio.strftime('%A')}")
print(f"Giờ phút giây hiện tại: {bay_gio.strftime('%H:%M:%S')}")


# ii. Tính số ngày cách nhau giữa 2 ngày nhập từ bàn phím
print("\n--- CÂU II: KHOẢNG CÁCH GIỮA 2 NGÀY ---")
try:
    print("Nhập ngày thứ nhất:")
    d1 = int(input("  Ngày: "))
    m1 = int(input("  Tháng: "))
    y1 = int(input("  Năm: "))
    
    print("Nhập ngày thứ hai:")
    d2 = int(input("  Ngày: "))
    m2 = int(input("  Tháng: "))
    y2 = int(input("  Năm: "))
    
    ngay_1 = date(y1, m1, d1)
    ngay_2 = date(y2, m2, d2)
    
    khoang_cach = abs((ngay_2 - ngay_1).days)
    print(f"=> Số ngày cách nhau giữa 2 ngày là: {khoang_cach} ngày")
except ValueError:
    print("Lỗi: Vui lòng nhập đúng định dạng số cho ngày/tháng/năm.")


# iii. Chuyển chuỗi S sang kiểu ngày (datetime object)
print("\n--- CÂU III: CHUYỂN CHUỖI SANG KIỂU NGÀY ---")
S = 'Sep 18 2019 2:43PM'
# %b: Tháng viết tắt, %d: Ngày, %Y: Năm 4 số, %I: Giờ (12h), %M: Phút, %p: AM/PM
doi_tuong_ngay = datetime.strptime(S, '%b %d %Y %I:%M%p')

print(f"Chuỗi S: '{S}'")
print(f"Kết quả sau khi chuyển: {doi_tuong_ngay}")
print(f"Kiểu dữ liệu: {type(doi_tuong_ngay)}")


# iv. Sử dụng timedelta để thêm 5 giây vào thời gian hiện tại
print("\n--- CÂU IV: SỬ DỤNG TIMEDELTA ---")
thoi_gian_truoc = datetime.now()
thoi_gian_sau = thoi_gian_truoc + timedelta(seconds=5)

print(f"Thời gian hiện tại:      {thoi_gian_truoc.strftime('%H:%M:%S')}")
print(f"Thời gian sau khi +5s:   {thoi_gian_sau.strftime('%H:%M:%S')}")
