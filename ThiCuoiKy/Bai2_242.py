# Kiểm tra số nguyên tố
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def in_bang_cuu_chuong(a, b):
    start = min(a, b)
    end = max(a, b)
    
    print(f"\n Bảng cửu chương từ {start} đến {end} ")
    for i in range(start, end + 1):
        print(f"\nBảng cửu chương {i}:")
        for j in range(1, 11):
            print(f"{i} x {j} = {i * j}")

# liệt kee số nguyên tố nhỏ hơn n
def liet_ke_snt_nho_hon_n(n):
    print(f"\n Các số nguyên tố nhỏ hơn {n} ")
    snt_list = []
    for i in range(2, n):
        if is_prime(i):
            snt_list.append(str(i))
    
    if snt_list:
        print(", ".join(snt_list))
    else:
        print(f"Không có số nguyên tố nào nhỏ hơn {n}.")

# liệt kê các ước số của n mà là số nt
def liet_ke_uoc_snt(n):
    print(f"\n Các ước số của {n} Là số nguyên tố")
    uoc_snt_list = []
    
    # Tìm các ước từ 1 đến n
    for i in range(1, n + 1):
        if n % i == 0:        
            if is_prime(i):   
                uoc_snt_list.append(str(i))
                
    if uoc_snt_list:
        print(f"Các số vừa là ước của {n}, vừa là số nguyên tố: " + ", ".join(uoc_snt_list))
    else:
        print(f"Không có ước số nào của {n} là số nguyên tố.")

# phan main
if __name__ == "__main__":
    # Nhập ab cách nhau bằng dấu plaayr
    try:
        input_ab = input("Nhập 2 số nguyên a, b (cách nhau bởi dấu phẩy): ")
        # Tách bằng dấu phẩy và chuyển thành số nguyên
        a, b = map(int, input_ab.split(','))
        in_bang_cuu_chuong(a, b)
    except ValueError:
        print("Vui lòng nhập đúng định dạng số nguyên và cách nhau bằng dấu phẩy (Ví dụ: 8,3 hoặc 3,8)")

    # Liệt kê các số nguyên tố nhỏ hơn n
    n1 = int(input("\nNhập số nguyên dương n để liệt kê các SNT < n: "))
    liet_ke_snt_nho_hon_n(n1)

    # Liệt kê ước của n là số nguyên tố
    n2 = int(input("\nNhập số nguyên dương n để tìm các ước là số nguyên tố: "))
    liet_ke_uoc_snt(n2)