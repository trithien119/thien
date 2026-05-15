def giai_ma_chuoi(cipher_text):
    plain_text = ""
    i = 0
    
    while i < len(cipher_text):
        if cipher_text[i] == '#':
            so_luong = int(cipher_text[i+1])
            ky_tu = cipher_text[i+2]

            plain_text += ky_tu * so_luong
            
            i += 3
        else:
            plain_text += cipher_text[i]
            i += 1
            
    return plain_text

vi_du_1 = "XY#6Z1#4023"
vi_du_2 = "#39+1=1#30"

print(f"Kết quả 1: {giai_ma_chuoi(vi_du_1)}")
print(f"Kết quả 2: {giai_ma_chuoi(vi_du_2)}")