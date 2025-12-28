# WHILE: vòng lặp vô hạn
# while <điều kiện> lặp lại cho đến điều kiện sai

# nhập số nguyên chẵn a --------------
a = input("nhập số nguyên chẵn a: ")
while(int(a) % 2 != 0 or int(a) < 0):
    a = input("Nhập lại một số chẵn: ")
print("Số chẵn a là", a)