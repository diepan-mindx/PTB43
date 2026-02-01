cart = []
funcs = [
    "0. In gio hang",
    "1. Them vao gio", 
    "2. Chinh sua mon hang",
    "3. Xoa mon hang (theo index)", 
    "4. Sap xep theo ten", 
    "5. Thoat chuong trinh"
        ]

# bat dau chuong trinh
print("-------------SHOPPING CART-------------")
while True:
    # in danh sach tinh nang
    print("---------------------------")
    for value in funcs:
        print(value)
    # chon 1 chuc nang
    choice = int(input("Chon 1 chuc nang: "))
    # neu khong chon dung -> bao loi
    while (choice > 5 or choice < 0):
        choice = int(input("Chon 1 chuc nang (0 -> 5): "))
        
    print("---------------------------")
    # func 5:
    if choice == 5:
        print("Bye!")
        break
    
    # func 0: in gio hang
    if choice == 0:
        if len(cart) == 0:
            print("Gio hang rong")
        else:
            for i in range(len(cart)):
                print(f"{i}: {cart[i]}")
    # func 1: them vao gio hang
    elif choice == 1:
        item = input("Nhap san pham:")
        cart.append(item)
        print("Da them thanh cong!")
    # func 2: chinh sua gio hang (index)
    elif choice == 2:
        if len(cart) == 0:
            print("Gio hang rong")
            continue
        index = int(input("Nhap index can sua: "))
        while index < 0 or index >= len(cart):
            index = int(input("Nhap index hop le: "))
        new_item = input("Nhap lai mon hang: ")
        cart[index] = new_item # the gia tri moi cho phan tu o index
        print("Da cap nhat thanh cong")
    # func 3: xoa mon hang (index)
    elif choice == 3:
        if len(cart) == 0:
            print("Gio hang rong")
            continue
        index = int(input("Nhap index can sua: "))
        while index < 0 or index >= len(cart):
            index = int(input("Nhap index hop le: "))
        del_item = cart.pop(index)
        print(f"Xoa thanh cong {del_item}")
    # func 4: sap xep theo ten
    elif choice == 4:
        cart.sort()
        print("Da sap xep thanh cong.")