# nhap giay -> HH: MM: SS
hour = 0
minute = 0
second = input("Nhap giay: ")

# chuyen kieu du lieu
second = int(second)

# tinh toan
hour = second // 3600 # lay phan nguyen
 # lay phan du khi chia voi gio
minute = (second % 3600) // 60
# phan le cua phut -> giay
second = (second % 3600) % 60

print(f"{hour}:{minute}:{second}")