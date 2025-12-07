# NOTE: toán tử Logic trả về 1 trong 2 vế
# NOTE: một số dữ liệu trả về False khi ép kiểu về Boolean:
# 1. Số 0
# 2. Chuỗi rỗng ""
# 3. Danh sách rỗng []
# 4. Giá trị None
# 5. Dữ liệu False
a = 10 # bool(a) -> True
b = 0 # false
c = "" # false
d = "hello" # true
# =========================
# and: trả về vế False, nếu k có False -> trả về vế 2
print(a and b)  # 0
print(a and d)  # hello

# =========================
# or: trả về vế True, nếu k có True -> trả về vế 2
print(c or b)  # 0
print(a or d)  # 10
# =========================
# not: phủ định: trả về true/ false
print(not a)  # False

