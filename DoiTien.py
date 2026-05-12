# Khai báo danh sách các loại tiền
cac_loai_tien = [500, 200, 100, 50, 20, 10, 5, 2, 1]

# Nhập số tiền X từ bàn phím
try:
    x = int(input("Nhap so tien X: "))
    so_tien_ban_dau = x
    
    so_to_tung_loai = []
    tong_so_to = 0

    # Duyệt qua từng loại tiền để tính số tờ
    for tien in cac_loai_tien:
        so_to = x // tien  # Lấy phần nguyên (số tờ)
        so_to_tung_loai.append(so_to)
        tong_so_to += so_to
        x %= tien      

    print(f"\nSo tien {so_tien_ban_dau} duoc doi thanh:")
    for i in range(len(cac_loai_tien)):
        print(f"Loai {cac_loai_tien[i]} gom {so_to_tung_loai[i]} to")
        
    print(f"TÔNG CỘNG CÓ {tong_so_to} TỜ")

except ValueError:
    print("Vui lòng nhập một số nguyên hợp lệ.")