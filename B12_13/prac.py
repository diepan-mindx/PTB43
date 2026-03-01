import math
# ham rut gon phan so
def rut_gon_phanso(tu:int, mau:int):
    # tim UCLN de chia cho tu va mau
    ucln = math.gcd(tu, mau)
    tu_moi = tu // ucln # chia lay so nguyen
    mau_moi = mau // ucln
    return tu_moi, mau_moi

# goi lai ham de chay
if __name__ == "__main__":
    print(rut_gon_phanso(6, 21))