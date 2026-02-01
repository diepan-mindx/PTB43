danhsach_diem = []
# them diem
so_bai_kiemtra = int(input("Nhap so bai kiem tra: "))
while so_bai_kiemtra <= 0: 
    so_bai_kiemtra = int(input("Nhap lai so bai kiem tra > 0: "))
    
for i in range(so_bai_kiemtra):
    diem = float(input(f"Nhap diem bai {i + 1}: "))
    while diem < 0:
        diem = float(input(f"Nhap lai diem hop le: "))
    # them vao danh sach
    danhsach_diem.append(diem)

print("Danh sach diem:", danhsach_diem)
# 1. Sắp xếp danh sách điểm số theo chiều tăng dần
danhsach_diem.sort(reverse=False)
print("Danh sach sau khi sort:", danhsach_diem)
# 2. Xoá số điểm nhỏ nhất (Nếu có hai số điểm nhỏ nhất thì xoá cả hai) 
if (so_bai_kiemtra == 1): print("Khong the xoa do danh sach 1 phan tu")
else:
    diem_nn = min(danhsach_diem)
    # lap toi khi xoa het diem nho nhat (neu trung)
    while diem_nn in danhsach_diem:
        danhsach_diem.remove(diem_nn)
print("Da xoa diem nho nhat:", diem_nn)
print("Danh sach sau khi xoa:", danhsach_diem)
# 3. Xuất danh sách điểm sau khi đã xử lý yêu cầu 1 và 2 
# 4. Đếm số lượng điểm lớn hơn hoặc bằng 8 và xuất ra màn hình
counter = 0
for value in danhsach_diem:
    if value >= 8: counter+=1
print("So luong diem >= 8:", counter)

danhsach_diem_lonhon_8 = [value for value in danhsach_diem if value >= 8]
print(len(danhsach_diem_lonhon_8)) # do dai danh sach diem >= 8