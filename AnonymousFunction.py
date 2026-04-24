import math

tri_tuyet_doi = lambda n: abs(n)

cong_15 = lambda n: n + 15

tich = lambda x, y: x * y

la_boi = lambda n: (n % 13 == 0) or (n % 19 == 0)

dt_tron = lambda r: 3.14 * r * r

cv_hcn = lambda d, r: (d + r) * 2

la_chinh_phuong = lambda n: n >= 0 and (math.sqrt(n) == int(math.sqrt(n)))

la_nguyen_to = lambda n: n > 1 and sum(1 for i in range(1, n + 1) if n % i == 0) == 2

loai_tam_giac = lambda a, b, c: (
    "Khong phai tam giac" if (a+b <= c or a+c <= b or b+c <= a) else
    "Tam giac Deu" if (a == b == c) else
    "Tam giac Can" if (a == b or b == c or a == c) else
    "Tam giac Vuong" if (a*a + b*b == c*c or a*a + c*c == b*b or b*b + c*c == a*a) else
    "Tam giac Thuong"
)

print("--- GIAI BAI TAP PYTHON ---")

n = int(input("Nhap vao mot so nguyen n: "))
print("- Tri tuyet doi:", tri_tuyet_doi(n))
print("- n + 15 =", cong_15(n))
print("- Co phai boi cua 13/19?", la_boi(n))
print("- Co phai so chinh phuong?", la_chinh_phuong(n))
print("- Co phai so nguyen to?", la_nguyen_to(n))

x = float(input("\nNhap x: "))
y = float(input("Nhap y: "))
print("- Tich x * y =", tich(x, y))

r = float(input("\nNhap ban kinh hinh tron: "))
print("- Dien tich hinh tron:", dt_tron(r))

dai = float(input("\nNhap chieu dai HCN: "))
rong = float(input("Nhap chieu rong HCN: "))
print("- Chu vi HCN:", cv_hcn(dai, rong))

print("\nNhap 3 canh tam giac:")
a = float(input("Canh 1: "))
b = float(input("Canh 2: "))
c = float(input("Canh 3: "))
print("- Ket qua:", loai_tam_giac(a, b, c))