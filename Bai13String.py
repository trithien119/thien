import re

def chuan_hoa_chuoi(s):
    s = s.strip()
    s = re.sub(r'\s+([.,])', r'\1', s)
    s = re.sub(r'([.,])(?=[^\s])', r'\1 ', s)
    s = re.sub(r'\s+', ' ', s)
    
    return s

def chuan_hoa_bai_tho(van_ban):
    cac_dong = van_ban.strip().split('\n')
    cac_dong_da_chuan_hoa = [chuan_hoa_chuoi(dong) for dong in cac_dong]
    return '\n'.join(cac_dong_da_chuan_hoa)

# --- CHẠY THỬ ---
du_lieu_vao = """
   Quê hương là   chùm  khế   ngọt .
  Cho  con  trèo  hái   mỗi  ngày  .  
Quê  hương là   đường  đi học .
   Con  về  rợp  bướm  vàng  bay .
   Đỗ    Trung  Quân   
"""

ket_qua = chuan_hoa_bai_tho(du_lieu_vao)
print(ket_qua)