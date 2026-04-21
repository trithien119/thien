from datetime import date

print("\n--- TÍNH KHOẢNG CÁCH NGÀY ---")
d1 = int(input("Nhập ngày 1: "))
m1 = int(input("Nhập tháng 1: "))
y1 = int(input("Nhập năm 1: "))

d2 = int(input("Nhập ngày 2: "))
m2 = int(input("Nhập tháng 2: "))
y2 = int(input("Nhập năm 2: "))

ngay1 = date(y1, m1, d1)
ngay2 = date(y2, m2, d2)

khoang_cach = abs((ngay2 - ngay1).days)
print(f"Kết quả: Hai ngày cách nhau {khoang_cach} ngày.")