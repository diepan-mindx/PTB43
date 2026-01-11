import math
# input: a, b
a = 0
b = 0
while (a and b) == 0:
    a = int(input("Nhap tu so: "))
    b = int(input("Nhap mau so: "))
    
# tinh boi chung nho nhat
bcnn = math.lcm(a, b)
print(f"BCNN cua {a} va {b} la: {bcnn}")

# rut gon phan so (ucln)
print(f"Phan so ban dau: {a}/{b}")
ucln = math.gcd(a, b)
a = a // ucln
b = b // ucln
print(f"Phan so rut gon: {a}/{b}")