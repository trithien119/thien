# du lieu dau vao cua nguoi dung
dai = float(input("Nhập chiều dài đáy hình khối chữ nhật (cm): "))
rong = float(input("Nhập chiều rộng đáy hình khối chữ nhật (cm): "))
cao = float(input("Nhập chiều cao hình khối chữ nhật (cm): "))
so_le = int(input("Số lượng số lẻ cần hiển thị: "))

# tinh dien tich day va the tich
dien_tich_day = dai * rong
the_tich = dien_tich_day * cao

# lam tron ket qua
dien_tich_day_tron = round(dien_tich_day, so_le)
the_tich_tron = round(the_tich, so_le)

# xuat ra man hinh bang ma UNICODE 
print(f"Diện tích đáy hình chữ nhật = {dien_tich_day_tron} cm\u00b2")
print(f"Thể tích hình khối = {the_tich_tron} cm\u00b3")