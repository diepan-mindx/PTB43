# Đề: nhập 2 số:
# 1. tìm số lớn hơn
# 2. tính tổng 2 số
# 3. chia lấy phần nguyên
# ===================================
# xác định kiểu dữ liệu 
# truyền 2 số vào từ bàn phím với input
a = input("a: ")
b = input("b: ")
print(a, type(a))
print(b, type(b))

# ===================================
# ép kiểu str -> int
# str -> float (có thể có dấu .)
# str -> int (không thể có dấu .)
# float -> int (bị bỏ phần thập phân - chỉ lấy phần nguyên)
a = int(a)
b = int(b)
print(type(a), type(b))

# ===================================
# 1. tìm số lớn hơn
if a > b:
    print("a là lớn hơn")
else:
    print("b là lớn hơn")

# ===================================
# 2. tính tổng 2 số
tong = a + b
print("Tổng 2 số:", tong)

# ===================================
# 3. chia lấy phần nguyên
chia_phan_nguyen = a//b
print("Chia a cho b, lấy phần nguyên:", chia_phan_nguyen)
chia_phan_du = a%b
print("Chia a cho b, lấy phần dư:", chia_phan_du)
