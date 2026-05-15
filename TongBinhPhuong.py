def tinh_tong_binh_phuong_so_con():
    # Nhập số nguyên dương n dưới dạng chuỗi để dễ cắt
    s_n = input("Nhập số nguyên dương n: ").strip()
    
    if not s_n.isdigit() or int(s_n) <= 0:
        print("Vui lòng nhập một số nguyên dương!")
        return

    tong_s = 0
    do_dai = len(s_n)
    danh_sach_so_con = []

    for length in range(do_dai, 0, -1):
        for i in range(do_dai - length + 1):
            sub_str = s_n[i : i + length]
            so_con = int(sub_str)

            tong_s += so_con**2
            danh_sach_so_con.append(f"{so_con}^2")

    print(f"\nTổng S = {' + '.join(danh_sach_so_con)}")
    print(f" => Kết quả cuối cùng: {tong_s}")

if __name__ == "__main__":
    tinh_tong_binh_phuong_so_con()