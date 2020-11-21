Username = input("Username :")
Password = input("Password : ")
if Username == "Naxocist" and Password == "1234":
    print("**** What is this shop ****")
    print("[1]Pen 15 THB")
    print("[2]Mouse 86 THB")
    print("[3]Eraser 5 THB")
    print("************")
    Userpick = int(input("Choose items >> "))
    Amount = int(input("Amount >>"))
    if Userpick == 1:
        print("Total :", 15 * Amount, "THB")
    elif Userpick == 2:
        print("Total :", 86 * Amount, "THB")
    else:
        print("Total :", 5 * Amount, "THB")
    print("****************")
    print("Thank you!")