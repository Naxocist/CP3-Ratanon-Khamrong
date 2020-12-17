menuList = []
priceList = []
def ShowBill():
    print("Restaurant".center(20, '-'))
    for i in range(len(menuList)):
        print(menuList[i], ":", priceList[i], "THB")
    print("*"*20)
    total = 0
    for x in range(len(priceList)):
        total += int(priceList[x])
    print("Total: ", total)
    print("Thank you!!!!")
while True:
    menuName = input("Please Enter Menu: ")
    if menuName.lower() == "exit":
        break
    else:
        menuPrice = input("Please Enter Price: ")
        menuList.append(menuName)
        priceList.append(menuPrice)

ShowBill()