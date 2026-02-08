# input: day diem (0 -> 10, cach = " ")
day_diem = input("Nhap day diem (0 -> 10, cach = ' '): ")
day_diem = day_diem.strip() # cat het khoang trang dau duoi
diem_parts = day_diem.split(' ')
# nhap sai format (khong phai so hoac ngoai khoang 0-10)
while True:
    valid = True
    for diem in diem_parts:
        diem = float(diem)
        if not ( 0<= diem <= 10):
            valid = False
            break
    
    if not valid:
        day_diem = input("Nhap lai day diem (0 -> 10, cach = ' '): ")
        day_diem = day_diem.strip() # cat het khoang trang dau duoi
        diem_parts = day_diem.split(' ')
    else:
        count_10 = 0
        # output: so diem 10 
        for diem in diem_parts:
            diem = float(diem)
            if diem == 10:
                count_10 += 1
                
        print(f"So diem 10 la: {count_10}") if count_10 > 0 else print("Khong co diem 10")
        break