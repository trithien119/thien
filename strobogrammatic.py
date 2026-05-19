import sys

def sieve_of_eratosthenes(limit):
    """Sàng Eratosthenes để kiểm tra số nguyên tố từ 0 đến limit-1."""
    is_prime = [True] * limit
    if limit > 0: is_prime[0] = False
    if limit > 1: is_prime[1] = False
    
    for p in range(2, int(limit**0.5) + 1):
        if is_prime[p]:
            for i in range(p * p, limit, p):
                is_prime[i] = False
    return is_prime

def is_strobogrammatic(num, extended=False):
    """Kiểm tra số Strobogrammatic gốc hoặc mở rộng sử dụng hai con trỏ."""
    s = str(num)
    left, right = 0, len(s) - 1

    valid_pairs = {
        ('0', '0'), ('1', '1'), ('8', '8'), 
        ('6', '9'), ('9', '6')
    }
    if extended:
        valid_pairs.add(('2', '5'))
        valid_pairs.add(('5', '2'))
        
    while left <= right:
        if (s[left], s[right]) not in valid_pairs:
            return False
        left += 1
        right -= 1
    return True

def rotate_180(num):
    """Xoay số 180 độ (bao gồm luật mở rộng). Trả về -1 nếu chứa số không hợp lệ."""
    s = str(num)
    mapping = {'0':'0', '1':'1', '8':'8', '6':'9', '9':'6', '2':'5', '5':'2'}
    
    rotated_chars = []
    for char in reversed(s):
        if char not in mapping:
            return -1
        rotated_chars.append(mapping[char])
        
    return int("".join(rotated_chars))

def print_sample(lst):
    """Hàm in rút gọn các câu có quá nhiều kết quả tránh tràn màn hình."""
    if len(lst) <= 30:
        print(", ".join(map(str, lst)))
    else:
        first_part = ", ".join(map(str, lst[:15]))
        last_part = ", ".join(map(str, lst[-15:]))
        print(f"{first_part}, ..., {last_part}")

def main():
    limit = 1000000
    print("--- ĐANG XỬ LÝ CÁC YÊU CẦU (VUI LÒNG CHỜ GIÂY LÁT) ---")

    is_prime = sieve_of_eratosthenes(limit)
    
    ans_a, ans_b, ans_c, ans_d, ans_e = [], [], [], [], []
    
    for i in range(1, limit):
        is_strob = is_strobogrammatic(i, extended=False)
        is_strob_ext = is_strobogrammatic(i, extended=True)
        
        # Câu a: Số strobogrammatic gốc
        if is_strob:
            ans_a.append(i)
            
        if is_strob and is_prime[i]:
            ans_b.append(i)
            
        if is_strob_ext:
            ans_c.append(i)
            
        if is_strob_ext and is_prime[i]:
            ans_d.append(i)

        if not is_strob_ext and not is_prime[i]:
            rotated = rotate_180(i)
            if rotated != -1 and is_prime[rotated]:
                ans_e.append(i)

    print(f"\na.- Số strobogrammatic nhỏ hơn 1 triệu (Tổng cộng: {len(ans_a)} số):")
    print_sample(ans_a)

    print(f"\nb.- Số nguyên tố strobogrammatic nhỏ hơn 1 triệu (Tổng cộng: {len(ans_b)} số):")
    print(", ".join(map(str, ans_b)))

    print(f"\nc.- Số strobogrammatic mở rộng nhỏ hơn 1 triệu (Tổng cộng: {len(ans_c)} số):")
    print_sample(ans_c)

    print(f"\nd.- Số nguyên tố strobogrammatic mở rộng nhỏ hơn 1 triệu (Tổng cộng: {len(ans_d)} số):")
    print(", ".join(map(str, ans_d)))

    print(f"\ne.- Số < 1 triệu không phải strob, không phải NT nhưng xoay 180 độ là số NT (Tổng cộng: {len(ans_e)} số):")
    print_sample(ans_e)

if __name__ == "__main__":
    main()