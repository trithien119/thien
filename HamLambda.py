import math


is_friendly = lambda n: math.gcd(n, int(str(n)[::-1])) == 1
is_perfect_square = lambda n: math.sqrt(n) % 1 == 0 if n >= 0 else False
is_uniform_all = lambda k: k > 0 and all(d == str(k)[0] for d in str(k))
is_uniform_any = lambda k: k > 0 and not any(d != str(k)[0] for d in str(k))
is_perfect_number = lambda n: n > 1 and sum(i for i in range(1, n // 2 + 1) if n % i == 0) == n
is_abundant = lambda x: x > 1 and sum(i for i in range(1, x // 2 + 1) if x % i == 0) > x
is_increasing = lambda x: all(str(x)[i] <= str(x)[i+1] for i in range(len(str(x)) - 1))
is_armstrong = lambda x: sum(int(d) ** len(str(x)) for d in str(x)) == x
is_lucky_all = lambda n: all(d in ['6', '8'] for d in str(n))
is_lucky_count = lambda n: str(n).count('6') + str(n).count('8') == len(str(n))

is_lucky_palindrome = lambda n: all(d in ['6', '8'] for d in str(n)) and str(n) == str(n)[::-1]


def main():
    while True:
        print("\n--- MENU KIỂM TRA SỐ ---")
        print("a. Số thân thiện")
        print("b. Số chính phương")
        print("c1. Số đồng nhất (all)")
        print("c2. Số đồng nhất (any)")
        print("d. Số hoàn thiện")
        print("e. Số phong phú")
        print("f. Số tăng dần")
        print("g. Số Armstrong")
        print("k1. Số lộc phát (all)")
        print("k2. Số lộc phát (count)")
        print("l. Số lộc phát Palindrome")
        print("0. Thoát")
        print("------------------------")
        
        chon = input("Nhập câu muốn chọn (a->l hoặc 0): ").strip().lower()
        
        if chon == '0':
            print("Thoát chương trình.")
            break
            
        if chon not in ['a', 'b', 'c1', 'c2', 'd', 'e', 'f', 'g', 'k1', 'k2', 'l']:
            print("Chọn sai rồi, nhập lại đi!")
            continue

        try:
            n = int(input("Nhập vào một số nguyên dương: "))
            if n < 0:
                print("Phải nhập số dương!")
                continue
        except ValueError:
            print("Lỗi: Phải nhập số nguyên!")
            continue

        print("-> Kết quả trả về:")
        if chon == 'a': 
            print(is_friendly(n))
        elif chon == 'b': 
            print(is_perfect_square(n))
        elif chon == 'c1': 
            print(is_uniform_all(n))
        elif chon == 'c2': 
            print(is_uniform_any(n))
        elif chon == 'd': 
            print(is_perfect_number(n))
        elif chon == 'e': 
            print(is_abundant(n))
        elif chon == 'f': 
            print(is_increasing(n))
        elif chon == 'g': 
            print(is_armstrong(n))
        elif chon == 'k1': 
            print(is_lucky_all(n))
        elif chon == 'k2': 
            print(is_lucky_count(n))
        elif chon == 'l': 
            print(is_lucky_palindrome(n))

        input("\nNhấn Enter để tiếp tục...")

if __name__ == "__main__":
    main()