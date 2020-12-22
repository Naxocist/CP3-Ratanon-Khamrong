menuList = []
def ShowBill():
    print("Restaurant".center(20, '-'))
    total = 0
    for i in range(len(menuList)):
        print(menuList[i][0], ":", menuList[i][1], "THB")
        total += int(menuList[i][1])
    print("*"*20)
    print("Total: ", total)
    print("Thank you!!!!")
while True:
    menuName = input("Please Enter Menu: ")
    if menuName.lower() == "exit":
        break
    else:
        menuPrice = input("Please Enter Price: ")
        menuList.append([menuName, menuPrice])

ShowBill()