s = input("Nhập chuỗi (S): ")
words = s.split()
seen = set()
result = None

for word in words:
    if word in seen:
        result = word
        break
    seen.add(word)

print(result)