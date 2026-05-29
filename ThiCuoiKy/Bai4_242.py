# số đồng nhất hàm all
is_homogenous_all = lambda k: all(d == str(k)[0] for d in str(k))

# số đồng nhất hàm any
is_homogenous_any = lambda k: not any(d != str(k)[0] for d in str(k))

# số hoàng thiện
is_perfect_number = lambda n: n == sum(i for i in range(1, n) if n % i == 0) and n > 0


# hàm main quét từ 1 tới 10000
if __name__ == "__main__":
    
# kiểm tra và in số đồng nhất
    print("Các số đồng nhất từ 1 đến 10000 bằng hàm all ")
    homo_list_all = [str(x) for x in range(1, 10001) if is_homogenous_all(x)]
    print(", ".join(homo_list_all))
    print()

    print("Các số đồng nhất từ 1 đến 10000 bằng hàm any")
    homo_list_any = [str(x) for x in range(1, 10001) if is_homogenous_any(x)]
    print(", ".join(homo_list_any))
    
    print("\n" + "="*60 + "\n")

    # Kiểm tra số hoàng thiện
    print("Các số hoàng thiện từ 1 đến 10000 ")
    perfect_list = [str(x) for x in range(1, 10001) if is_perfect_number(x)]
    
    if perfect_list:
        print(", ".join(perfect_list))
    else:
        print("Không tìm thấy số hoàn thiện nào.")