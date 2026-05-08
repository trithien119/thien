s = input("Nhập số điện thoại (S): ")
all_digits = set("0123456789")
input_digits = set(s)

missing = sorted(list(all_digits - input_digits))
print(missing)