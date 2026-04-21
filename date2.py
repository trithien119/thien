from datetime import date

print("\n--- Nhập ngày tháng cho 2 mốc thời gian ---")
d1 = int(input("Ngày 1: "))
m1 = int(input("Tháng 1: "))
y1 = int(input("Năm 1: "))

d2 = int(input("Ngày 2: "))
m2 = int(input("Tháng 2: "))
y2 = int(input("Năm 2: "))

date1 = date(y1, m1, d1)
date2 = date(y2, m2, d2)

delta = abs(date2 - date1)
print(f"Số ngày cách nhau giữa 2 ngày là: {delta.days} ngày")