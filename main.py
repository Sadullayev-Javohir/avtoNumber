from seller import *
from user import *


def main():
    print()
    print("1.Sotuvchi Menyusi")
    print("2.Foydalanuvchi Menyusi")
    print("3.Chiqish")
    print()
    prompt = input("Tanlang: ")

    if prompt == "1":
        sellerRun()
    elif prompt == "2":
        user()
    elif prompt == "3":
        print("Kuningiz yaxshi o'tsin")
        return
    else:
        print("1-3 gacha raqam kiriting: ")
        return main()
if __name__ == "__main__":
    main()