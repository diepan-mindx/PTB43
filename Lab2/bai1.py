RED = '\033[31m'
GREEN = '\033[32m'
YELLOW = '\033[33m'
RESET = '\033[0m'
# nhap tu ban phim d, r
print(RED +"--- Hinh chu nhat ---" + RESET)
d = float(input(GREEN + "Nhap chieu dai: " + RESET))
r = float(input(GREEN + "Nhap chieu rong: " + RESET))
# chu vi
cv = 2 * (d + r)
print(YELLOW + "Chu vi hinh chu nhat: " + RESET, cv)
# dien tich 
dt = d * r
print(YELLOW + "Dien tich hinh chu nhat: " + RESET, dt)