# cau_kiem_tra : so_hoc_sinh = ? du ?
cau_kiem_tra = input("Nhap so cau kiem tra: ")
so_hoc_sinh = input("Nhap so hoc sinh: ")

# chuyển kiểu dữ liệu
cau_kiem_tra = int(cau_kiem_tra)
so_hoc_sinh = int(so_hoc_sinh)

# kết luận 
print(f"""Mỗi học sinh sẽ được làm {cau_kiem_tra//so_hoc_sinh} câu kiểm tra, 
còn dư {cau_kiem_tra%so_hoc_sinh} câu kiểm tra""")