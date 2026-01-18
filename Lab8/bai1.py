# xac dinh canh tam giac
# input: do dai 3 canh a, b, c
a = -1
b = -1
c = -1
while (a or b or c) <= 0:
    print("--------------------------------")
    print("Nhap do dai 3 canh tam giac (a, b, c > 0): ")
    a = int(input("Nhap do dai canh a (a > 0): "))
    b = int(input("Nhap do dai canh b (b > 0): "))
    c = int(input("Nhap do dai canh c (c > 0): "))

if a + b > c and a + c > b and b + c > a:
    print("3 canh tren tao thanh 1 tam giac")
else:
    print("3 canh tren khong tao thanh 1 tam giac")