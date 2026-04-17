dai = float(input("Nhập chiều dài đáy hình chữ nhật (cm): "))
rong = float(input("Nhập chiều rộng đáy hình chữ nhật (cm): "))
cao = float(input("Nhập chiều cao hình khối (cm): "))
sole = input ("số lượng số lẻ cần hiển thị:")
dinhdang = '{:.' +sole+'f}'

dai = float(dinhdang.format(eval(dai)))
rong = float(dinhdang.format(eval(rong)))
cap = float(dinhdang.format(eval(cao)))

dientich = dai*rong
dientich = float(dinhdang.format(dientich))
thetich = dai*rong*cao
thetich = float(dinhdang.format(thetich))

print ("Diện tích đáy hình chữ nhật = ",dientich,"cm\u00b2")
print ("Thể tích hình khối = ","cm\u00b3")