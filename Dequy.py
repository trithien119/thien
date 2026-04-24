def tong_chu_so(n):
    if n < 10:
        return n
    return n % 10 + tong_chu_so(n // 10)

def giai_thua(n):
    if n == 0 or n == 1:
        return 1
    return n * giai_thua(n - 1)

def luy_thua(a, b):
    if b == 0:
        return 1
    return a * luy_thua(a, b - 1)

def USCLN(a, b):
    if b == 0:
        return a
    return USCLN(b, a % b)

def fibonacci(n):
    if n == 0 or n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)


print("--- KIỂM TRA HÀM ĐỆ QUY ---")

n1 = int(input("1) Nhập n để tính tổng chữ số: "))
print(f"-> Tổng các chữ số: {tong_chu_so(n1)}")

n2 = int(input("\n2) Nhập n để tính giai thừa: "))
print(f"-> {n2}! = {giai_thua(n2)}")

a3 = int(input("\n3) Nhập cơ số a: "))
b3 = int(input("   Nhập số mũ b: "))
print(f"-> {a3}^{b3} = {luy_thua(a3, b3)}")

a4 = int(input("\n4) Nhập số nguyên dương a: "))
b4 = int(input("   Nhập số nguyên dương b: "))
print(f"-> USCLN của {a4} và {b4} là: {USCLN(a4, b4)}")

n5 = int(input("\n5) Nhập n để tìm số Fibonacci thứ n: "))
print(f"-> F({n5}) = {fibonacci(n5)}")