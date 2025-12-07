# tao tam giac vuong * voi n dong (> 1)
# input n
n = input("So dong > 1: ") # str
n = int(n) # int
if (n < 2):
    print("So dong phai lon hon 1")
else:
    # tao tam giac vuong *
    for i in range(1, n+1):
        print("* "*i)

