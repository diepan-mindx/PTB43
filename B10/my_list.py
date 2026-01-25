danh_sach_1 = [1, "a", "abc123",1, 12.3, False]
# -----------------------------------
# Duyệt danh sách
for i in range(len(danh_sach_1)):
    print(danh_sach_1[i])

# dung khi khong can index    
for value in danh_sach_1:
    print(value)
# -----------------------------------
# Thêm mới phần tử
# append(value): them vao cuoi phan tu
danh_sach_1.append(100)
print(danh_sach_1)
# insert(index, value): them vao vi tri index 
danh_sach_1.insert(len(danh_sach_1) -1, "new")
print(danh_sach_1)
# -----------------------------------
# Sửa phần tử
danh_sach_1[4] = "updated item"
print(danh_sach_1)
# -----------------------------------
# Xóa phần tử
# pop(): xoa o vi tri cuoi cung cua danh sach -> tra ve phan tu bi xoa
del_item = danh_sach_1.pop()
print(f"{del_item} da duoc xoa khoi danh sach {danh_sach_1}")
# pop(index): xoa o vi tri index -> tra ve phan tu bi xoa
del_item_1 = danh_sach_1.pop(-1)
print(f"{del_item_1} da duoc xoa khoi danh sach {danh_sach_1}")
# remove(value): xoa phan tu co value trung khop (neu co nhieu phan tu giong -> xoa o trai)
# NOTE: remove tra ve loi neu khong co phan tu nay
del_item_2 = danh_sach_1.remove(1)
print(danh_sach_1)
# clear(): xoa het danh sach
# print(danh_sach_1.clear())
# -----------------------------------
# Sắp xếp danh sách
# sort(reverse=?): neu ? la False: tang dan | ? la True: giam dan
# NOTE: nếu muốn sắp xếp -> cùng kiểu dữ liệu trong danh sách
danh_sach_2 = ['a', 'm', 'A', 'x', '-']

danh_sach_2.sort(reverse=True)
print(danh_sach_2) # giam dan
danh_sach_2.sort(reverse=False)
print(danh_sach_2) # tang dan
