# ỨNG DỤNG tạo câu hỏi tính toán 
# cách chơi:
# 1. start
# 2. exit (break)
# 3. skip (continue/ pass)
# 3. nhập số lượng câu hỏi: n (for)
# $. nếu trả lời sai -> bắt người dùng trả lời lại (while)
# -----------------------------
import random

# bat dau choi
while True:
    choice = input("Nhập 'start' để chơi, 'exit' để thoát: ")
    choice = choice.lower().strip() # chuyen ve chu thuong + xoa het khoang trang dau cuoi
    # truong hop ngoai le lam truoc
    if choice == 'exit':
        print("Chương trình kết thúc, Byee!")
        break
    if choice != 'start':
        print("Lựa chọn không hợp lệ!")
        continue
    # so luong cau hoi
    # input: n
    n = int(input("Nhập số lượng câu hỏi: "))
    while n <= 0:
        print("Số lượng câu hỏi phải lớn hơn 0")
        n = int(input("Nhập lại số lượng câu hỏi: "))
    # tao cau hoi dua tren so luong cau hoi
    for so_lan in range(1, n + 1):
        a = random.randint(1, 10)
        b = random.randint(1, 10)
        correct = a + b
        # in cau hoi
        question = f"{a} + {b} = "
        ans = ""
        # kiem tra cau tra loi
        while(ans == ""):
            ans = input(question)
            if ans.lower().strip() == "skip":
                print("Đã bỏ qua câu hỏi này!")
                break
            if int(ans) == correct:
                print("Đúng ->")
                break
            else:
                print("Sai xx")
                ans = "" 