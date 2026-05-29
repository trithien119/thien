#ham lambda kiểm tra có phải là bội số của 13 hoặc 19 hay không
kiem_tra_boi_so = lambda n: n % 13 == 0 or n % 19 == 0

# Hàm lambda kiểm tra và phân loại tam giác
phan_loai_tam_giac = lambda a, b, c: (
    "Không phải tam giác hợp lệ" if not (a + b > c and a + c > b and b + c > a) else (
        "Tam giác đều" if a == b == c else (
            "Tam giác vuông" if (a**2 + b**2 == c**2 or a**2 + c**2 == b**2 or b**2 + c**2 == a**2) else (
                "Tam giác cân" if (a == b or b == c or a == c) else "Tam giác thường"
            )
        )
    )
)

# hàm main để chạy
if __name__ == "__main__":  
    # Chạy và nhập để kiểm tra có phải là bội số của 13 hoặc 19
    num = int(input("Nhập vào số nguyên n cần kiểm tra bội số: "))
    if kiem_tra_boi_so(num):
        print(f"-> Số {num} LÀ bội số của 13 hoặc 19.")
    else:
        print(f"-> Số {num} KHÔNG PHẢI là bội số của 13 hoặc 19.")
    print("-" * 40)
    
    # nhập thông số của từng cạnh vào
    print("Nhập 3 cạnh của tam giác (a, b, c):")
    a = int(input("Nhập cạnh a: "))
    b = int(input("Nhập cạnh b: "))
    c = int(input("Nhập cạnh c: "))
    
    ket_qua_tam_giac = phan_loai_tam_giac(a, b, c)
    print(f"-> Kết quả phân loại: {ket_qua_tam_giac}")