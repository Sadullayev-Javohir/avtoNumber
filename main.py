from seller import *
from user import *


def main():
    print()
    print("Avto Raqam")
    print()
    print("1.Sotuvchi Menyusi")
    print("2.Foydalanuvchi Menyusi")
    print("3.Chiqish")
    print()
    prompt = input("Tanlang: ")

    if prompt == "1":
        def passwordCheck():
            password = input("Parol kiriting: ")
            if password == "12345":
                sellerRun()
                return
            else:
                print()
                print("Xato qaytadan kiriting: ")
                print()
                passwordCheck()
        passwordCheck()
        
    elif prompt == "2":
        def passwordCheck():
            password = input("Parol kiriting: ")

            if password == "1234":
                user()
                return
            else:
                print()
                print("Xato qaytadan kiriting: ")
                print()
                passwordCheck()
        passwordCheck()
    elif prompt == "3":
        print("Kuningiz yaxshi o'tsin")
        return
    else:
        print("1-3 gacha raqam kiriting: ")
        return main()
if __name__ == "__main__":
    main()