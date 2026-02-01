# ------------------------------------
# khai bao sau ki tu
chuoi_rong = ""
fullName = "Ma Ky Ky"
# ------------------------------------
# do dai chuoi
print(len(chuoi_rong))
print(len(fullName))
# ------------------------------------
# duyet xau
for chart in fullName:
    print(chart, end="")

for index in range(len(fullName)):
    # truy cap phan tu  
    print(f"{index}: {fullName[index]}")
# ------------------------------------
# + xau ki tu
sentence = "My fullname is " + fullName + "."
print(sentence)
# ------------------------------------
# xau con 
firstName = "Ma"
lastName = "diep"
# ------------------------------------
# tim xau con trong danh sach (in)
print(firstName in fullName) # true
print(lastName in fullName) # false
# ------------------------------------
# chinh kieu cho string
print(fullName.lower()) # chuyen het ki tu thanh chu thuong
print(fullName.upper()) # chuyen het ki tu thanh chu hoa
print(fullName.capitalize()) # viet hoa chu cai dau tien trong str
# ------------------------------------
# tim vi tri xau con (find)
d_index = fullName.find("d")
print(d_index) # khong co tra ve -1
# NOTE: find(ki tu can tim, start, stop)
k_index = fullName.find("K", 4) # neu trung ki tu thi lay ki tu dau tien (start, stop)
print(k_index)
# ------------------------------------
# str -> list (split)
nameList = fullName.split(" ")
print(nameList)
# ------------------------------------
# thay doi phan tu (gia tri)
# replace(gia tri can thay, gia tri moi, so luong can thay) -> ham co return
# NOTE: neu khong co <so luong can thay> -> sua het 
newName = fullName.replace("Ky", "Diep", 1)
print(newName)