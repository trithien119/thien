import math

def so_dao_nguoc(n):
    return int(str(n)[::-1])

def ucln(x, y):
    return math.gcd(x, y)

def giai_quyet():
    try:
        a = int(input("Nhập a (>= 10): "))
        b = int(input("Nhập b (<= 30000): "))
        
        if not (10 <= a <= b <= 30000):
            print("Vui lòng nhập đúng điều kiện 10 <= a <= b <= 30000")
            return

        danh_sach_than_thien = []

        for i in range(a, b + 1):
            dao = so_dao_nguoc(i)
            if ucln(i, dao) == 1:
                danh_sach_than_thien.append(i)

        print("\nCác số thân thiện trong khoảng từ", a, "đến", b, "là:")
        print(*danh_sach_than_thien)
        
        print(f"\nTổng cộng có {len(danh_sach_than_thien)} số thân thiện.")
        
    except ValueError:
        print("Vui lòng chỉ nhập số nguyên.")

if __name__ == "__main__":
    giai_quyet()