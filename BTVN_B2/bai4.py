n=int(input("Nhap vao so luong xu: "))
while n<28:
    print("So xu khong hop le.")
    n=int(input("Nhap vao so luong xu: "))
sochaibia=n//28
vochai=sochaibia
tong=sochaibia
while vochai>=3:
    doi=vochai//3
    tong+=doi
    vochai=vochai%3+doi
print("Tien thua:",n-sochaibia*28)
print("So chai bia co the mua duoc la: ",tong)