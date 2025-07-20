a= int(input("Nhập năm: "))
while a<1582:
    print("Không hợp lệ, hãy nhập lại")
    a= int(input("Nhập vào năm muốn biết: "))
b= int(input("Nhập tháng của năm đó: "))
while b<1 or b>12:
    print("Nhập lại:")
    b=int(input("Nhập vào tháng của năm:"))
if a%400==0 and b==2:
    print("Có 29 ngày")
elif (b<=7 and b%2==1) or (b>8 and b%2==0):
    print("Có 31 ngày")
else:
    print("Có 30 ngày")