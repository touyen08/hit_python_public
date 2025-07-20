a= int(input("Nhập lương nhân viên(triệu đồng): "))
if a>15:
    tienluong = a-a*0.3
    print("Tiền lương của nhân viên là: ",tienluong)
elif 7<=a<=15:
    tienluong = a-a*0.2
    print("Tiền lương của nhân viên là: ",tienluong)
elif a<7:
    tienluong = a-a*0.1
    print("Tiền lương của nhân viên là: ",tienluong)