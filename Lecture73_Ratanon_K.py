menuList = []
Permanentmenu = {"Fried chicken": 23, "Vegetable": 65, "Cheese": 55}
def ShowBill():
    print("High - Quality : Restaurant".center(20, '-'))
    total = 0
    for i in range(len(menuList)):
        print(menuList[i][0], ":", menuList[i][1], "THB")
        total += int(menuList[i][1])
    print("*"*20)
    print("Total :", total, "THB")
    print("Thank you!!!!")
while True:
    menuName = input("Please Enter Menu: ")
    if menuName.lower() == "exit":
        break
    else:
        menuList.append([menuName, Permanentmenu[menuName]])

ShowBill()