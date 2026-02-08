# input: dd/mm/yyyy
date_str = input("Nhap ngay thang nam (dd/mm/yyyy): ")
date_parts = date_str.split('/')
# nhap sai format (thieu 1 trong 3 phan)
while len(date_parts) != 3:
    date_str = input("Nhap lai ngay thang nam (dd/mm/yyyy): ")
    date_parts = date_str.split('/')
# kiem tra ngay/ thang/ nam co hop le khong
day = int(date_parts[0])
month = int(date_parts[1])
year = int(date_parts[2])

if not (1 <= day <= 31) or not (1 <= month <=12) or year < 0:
    print("Ngay thang nam khong hop le.")
else:
    # output: ngay dd, thang mm, nam yyyy
    print(f"Ngay {day:02d}, thang {month:02d}, nam {year}")
    

