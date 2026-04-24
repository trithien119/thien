import math

abs_val = lambda n: abs(n)
add_15 = lambda n: n + 15
multiply = lambda x, y: x * y
is_multiple = lambda n: n % 13 == 0 or n % 19 == 0
circle_area = lambda r: math.pi * r**2
rect_perimeter = lambda d, r: (d + r) * 2
is_perfect_square = lambda n: n >= 0 and math.isqrt(n)**2 == n
is_prime = lambda n: n > 1 and all(n % i != 0 for i in range(2, int(math.sqrt(n)) + 1))
classify_triangle = lambda a, b, c: (
    "Không phải tam giác" if not (a + b > c and a + c > b and b + c > a) else
    "Tam giác đều" if a == b == c else
    "Tam giác cân" if a == b or b == c or a == c else
    "Tam giác vuông" if round(a**2 + b**2, 5) == round(c**2, 5) or \
                         round(a**2 + c**2, 5) == round(b**2, 5) or \
                         round(b**2 + c**2, 5) == round(a**2, 5) else
    "Tam giác thường"
)

print("--- KIỂM TRA CÁC BÀI TẬP LAMBDA ---")

n = int(input("\nNhập số nguyên n: "))
print(f"a) Trị tuyệt đối: {abs_val(n)}")
print(f"b) n + 15 = {add_15(n)}")
print(f"d) Có là bội của 13 hoặc 19? {'Có' if is_multiple(n) else 'Không'}")
print(f"g) Có là số chính phương? {'Có' if is_perfect_square(n) else 'Không'}")
print(f"h) Có là số nguyên tố? {'Có' if is_prime(n) else 'Không'}")

x = float(input("\nNhập x: "))
y = float(input("Nhập y: "))
print(f"c) Tích x * y = {multiply(x, y)}")

r = float(input("\nNhập bán kính hình tròn r: "))
print(f"e) Diện tích hình tròn: {circle_area(r):.2f}")

d = float(input("\nNhập chiều dài HCN: "))
r_hcn = float(input("Nhập chiều rộng HCN: "))
print(f"f) Chu vi hình chữ nhật: {rect_perimeter(d, r_hcn)}")

print("\nNhập 3 cạnh của tam giác:")
a = float(input("Cạnh a: "))
b = float(input("Cạnh b: "))
c = float(input("Cạnh c: "))
print(f"i) Kết quả: {classify_triangle(a, b, c)}")