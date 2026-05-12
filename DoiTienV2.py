tien = [500, 200, 100, 50, 20, 10, 5, 2, 1]

def tinh_doi_tien(so_tien):
    tong_so_to = 0
    so_loai = 0
    
    print(f"\nSo tien {so_tien} duoc doi thanh:")
    
    for mệnh_giá in tien:
        so_to = so_tien // mệnh_giá
        if so_to > 0:
            print(f"Loai {mệnh_giá} gom {so_to} to")
            tong_so_to += so_to
            so_loai += 1
        so_tien %= mệnh_giá
        
    print(f"TONG CONG CO {tong_so_to} TO")
    print(f"Tong so loai = {so_loai}")

try:
    a = int(input("Nhap so tien hang can phai tra (a): "))
    b = int(input("Nhap so tien khach hang thuc te tra (b): "))

    if a > b:
        print(f"So tien khach hang con thieu la: {a - b}")
    elif a == b:
        print("Cam on khach hang. Hen gap lai")
    else:
        tien_thua = b - a
        print(f"Tien thua can thoi lai: {tien_thua}")
        
        tinh_doi_tien(tien_thua)
        
        input("\nNhan Enter de ket thuc chuong trinh...")
        print("Cam on khach hang. Hen gap lai")

except ValueError:
    print("Vui lòng nhập số nguyên hợp lệ!")