# input: nhap thang, nam
# output: so ngay trong thang do
import datetime
year = -1
month = -1
now = datetime.datetime.now()
days = 0

# nhap nam
while  (year <= 0):
    year = int(input("Nhap nam (nam > 0): "))

# nhap thang
while (month < 1 or month > 12):
    month = int(input("Nhap thang (1-12): "))

# tinh so ngay trong thang
if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
    days = 31
elif month == 4 or month == 6 or month == 9 or month == 11:
    days = 30
else:
    # tinh nam nhuan
    if (year % 4 == 0 and year % 100 != 0):
        days = 29
    else:
        days = 28

# output: so ngay trong thang
print("-------------------------")
print(f"Thang {month} nam {year} co {days} ngay.")
