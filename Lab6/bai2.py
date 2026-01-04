# in ra cac so chan tu 1 den n
n = -1
while n <= 0:
     n = int(input("Nhap so nguyen > 0: "))

# [<gia tri can tra ve> for i in range(...) if <dieu kien>]
danh_sach_chan = [i for i in range(1, n + 1) if i % 2 == 0]
print(f"Danh sach so chan tu 1 den {n} la: {danh_sach_chan}")