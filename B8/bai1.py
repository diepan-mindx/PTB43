# n ? nguyen to ( > 2, so nguyen)
n = -1
while n < 2:
    n = int(input("Nhap mot so nguyen >= 2: "))
la_so_nguyen_to = True
for i in range(2, (n//2) + 1):
    if n % i == 0:
        la_so_nguyen_to = False
        break
# in ket qua
if la_so_nguyen_to == False:
    print(f"{n} khong phai la so nguyen to.")
else:
    print(f"{n} la so nguyen to.")