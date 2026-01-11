# input: chon tai khoan + nhập mật khẩu
# neu nhap qua 5 lan sai -> khoa tai khoan
# output: thong bao dang nhap thanh cong/that bai
acc_pass_1 = "123456"
acc_pass_2 = "654321"
acc_pass_3 = "Diep@123"
# nhan "exit" de thoat chuong trinh

while True:
    # chon tai khoan
    print("Chon tai khoan de dang nhap:")
    print("1. Tai khoan 1"
          "\n2. Tai khoan 2"
          "\n3. Tai khoan 3")
    acc_choice = int(input("Nhap so tai khoan (1-3): "))
    while acc_choice < 1 or acc_choice > 3:
        acc_choice = int(input("Lua chon khong hop le. Vui long nhap so tai khoan (1-3): "))

    khoa_tai_khoan = False
    pass_input = input("Nhap mat khau (hoac nhan 'exit' de thoat): ")
    # kiem tra mat khau (toi da 5 lan nhap sai)
    for turn in range(5):
        if acc_choice == 1:
            correct_pass = acc_pass_1
        elif acc_choice == 2:
            correct_pass = acc_pass_2
        elif acc_choice == 3:
            correct_pass = acc_pass_3
        # hoi mat khau
        while pass_input == "":
            pass_input = input("Nhap mat khau (hoac nhan 'exit' de thoat): ")
            
        if pass_input.lower() == "exit":
            print("Thoat chuong trinh.")
            break
        if turn == 4:
            print("Ban da nhap sai qua 5 lan. Tai khoan bi khoa.")
            khoa_tai_khoan = True
            break
        # check password
        if pass_input == correct_pass:
            print("Dang nhap thanh cong!")
            break
        else:
            pass_input = ""
            print(f"Mat khau sai, ban con {5 - turn} lan thu lai.")
           
           
    
    # neu sai qua 5 lan -> thoat chuong trinh 
    if khoa_tai_khoan or pass_input.lower() == "exit":
        break
    
