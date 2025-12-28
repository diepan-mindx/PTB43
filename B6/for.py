# FOR: vòng lặp hữu hạn 
# range(start, stop, step)
# lặp lại trong khoảng từ <start> -> <stop - 1>, bước nhảy là <step> đơn vị
# -------------
# range(stop): lặp lại từ 0 -> stop - 1, mặc định bước nhảy là 1
# range(start, stop): lặp lại từ start -> stop - 1, mặc định bước nhảy là 1
# range(start, stop, step)

# countdown 10s happy new year ----------------------
import time

for giay in range(10, 0, -1):
    print(giay)
    time.sleep(1)

print("Happy new Year")

# ve tam giac ---------------------------------------
canh = 6
for dong in range(1, canh + 1):
    print(" " * (canh - dong) + "0 " * dong)
    
print("Merry Christmas")