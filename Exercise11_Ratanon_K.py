number = int(input("Level of the pyramid: "))
for i in range(number):
    star = ""
    print(" " * (number-i), end="")
    for j in range((i+1)*2-1):
        star += "*"
    print(star)