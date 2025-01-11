import json
from datetime import datetime

# Hozirgi vaqtni olish
purchaseTime = datetime.now()


lastID = 0

# keyingi ID ni olish
def nextID():
    global lastID
    lastID += 1
    return lastID

# oxirgi ID
def LoadLastID():
    global lastID  
    try:
        with open("users.json", "r") as json_file:
            soldNumList = json.load(json_file)
            if soldNumList:
                lastID = max(item["ID"] for item in soldNumList)
    except(FileNotFoundError, ValueError):
        lastID = 0

# foydalanuvchi ma'lumotlarini saqlash
def saveToJson():
    with open("users.json", "w") as json_file:
        json.dump(soldNumList, json_file, indent=4)
    

# Sotuvchining ma'lumotlarini yangilash
def saveToSellerJson():
    with open("numbers.json", "w") as json_file:
        json.dump(numberList, json_file, indent=4)


# barcha tarixlarni saqlash
def saveToMainHistoryJson():
    with open("mainHistory.json", "w") as json_file:
        json.dump(mainHistoryList, json_file, indent=4)

# barcha tarixlarni o'qish
def mainHistoryJsonRead():
    global mainHistoryList
    try:
        with open("mainHistory.json", "r") as json_file:
            mainHistoryList = json.load(json_file)
    except json.JSONDecodeError:
        
        mainHistoryList = []


# numberList dagi ma'lumotlarni o'qish
def JsonRead():
    global numberList
    try:
        with open("numbers.json", "r") as json_file:
            numberList = json.load(json_file)
    except json.JSONDecodeError:
        numberList = []

# foydalanuvchi ma'lumotlarini o'qish
def UsersJsonRead():
    global soldNumList
    try:
        with open("users.json", "r") as json_file:
            soldNumList = json.load(json_file)
    except json.JSONDecodeError:
        soldNumList = []


# foydalanuvchi ismini tekshirish
def usernameCheck():
    username = input("Ismingizni kiriting: ")

    if username.isalpha() == True and username[0].isupper() == True and len(username) > 2:
        return username
    else:
        return usernameCheck()


# foydalanuvchi ismini tekshirish
def addressnameCheck():
    address = input("Manzilingizni kiriting: ")

    if address.isalpha() == True and address[0].isupper() == True and len(address) > 2:
        return address
    else:
        return addressnameCheck()


numberList = []
soldNumList = []

mainHistoryDic = {}
mainHistoryList = []

soldNumDic = {}



JsonRead()

UsersJsonRead()

mainHistoryJsonRead()

LoadLastID()



# 1. Mavjud raqamlarni ko'rish
def viewNum():
    if numberList == []:
        print()
        print("Hali ma'lumotlar yo'q")
        print()
        return
    for numDic in numberList:
        print()
        print(f"ID: {numDic["ID"]}, Avtoraqam: {numDic["number"]}, Narxi: {numDic["cost"]} so'm, Qo'yilgan vaqti: {numDic["putTime"]}, Xolati: {numDic["status"]}")
        print()

# 2. Raqam sotib olish
def buyNum():
    if numberList == []:
        print()
        print("Hali ma'lumotlar yo'q")
        print()
        return
    
    viewNum()
    inputNum = input("Sotib olmoqchi bo'lgan avtoraqamni kiriting: ")

    while True:
        for i in range(len(numberList)):
            if numberList[i]["number"] == inputNum:
                userName = usernameCheck()
                userAddress = addressnameCheck()
                numberList[i]["status"] = "Sotilgan"
                soldNumDic = {
                    "ID": nextID(),
                    "userName": userName,
                    "userAddress": userAddress,
                    "soldNumber": numberList[i]["number"],
                    "soldTime": purchaseTime.strftime("%Y-%m-%d %H:%M:%S"),
                }
                mainHistoryDic = {
                    "AvtoNumberID": numberList[i]["ID"],
                    "AvtoNumber": numberList[i]["number"],
                    "AvtoNumberCost": numberList[i]["cost"],
                    "AvtoNumberPutTime": numberList[i]["putTime"],
                    "AvtoNumberStatus": numberList[i]["status"],
                    "userID": soldNumDic["ID"],
                    "userName": soldNumDic["userName"],
                    "userAddress": soldNumDic["userAddress"],
                    "AvtoNumberSoldTime": soldNumDic["soldTime"]

                }
                soldNumList.append(soldNumDic)

                mainHistoryList.append(mainHistoryDic)
                del numberList[i]

                saveToJson()
                saveToSellerJson()
                saveToMainHistoryJson()

                print()
                print("Muvaffaqqiyatli sotib oldingiz")
                print()
                return
        else:
            print("Xato...")
            inputNum = input("Sotib olmoqchi bo'lgan avtoraqamni kiriting: ")
            

# 3. Xarid tarixini ko'rish
def buyHistory():
    if soldNumList == []:
        print()
        print("Hali xarid qilmagansiz")
        print()
    else:
        for soldNumDic in soldNumList:
            print()
            print(f"ID: {soldNumDic["ID"]}, Foydalanuvchi ismi: {soldNumDic["userName"]}, Manzili: {soldNumDic["userAddress"]}, Sotilgan vaqti: {soldNumDic["soldTime"]}")
            print()


def user():
    print("Foydalanuvchi Menyusi:")
    print("1. Mavjud raqamlarni ko'rish")
    print("2. Raqam sotib olish")
    print("3. Xarid tarixini ko'rish")
    print("4. Chiqish")

    choose = input("Tanlang: ")

    if choose == "1":
        viewNum()
        user()
    elif choose == "2":
        buyNum()
        user()
    elif choose == "3":
        buyHistory()
        user()
    elif choose == "4":
        print()
        print("Kuningiz yaxshi o'tsin")
        print()
        return
    else:
        print("1-4 gacha son kiriting: ")
        user()

