# Đếm số ký tự trong chuỗi:
def demchuoi(txt):
    dem=0
    for i in txt:
        dem+=1
    return dem
nhapchuoi=input("Nhập chuỗi của bạn vào: ")
print('Độ dài của chuỗi là: ',demchuoi(nhapchuoi))
