from tkinter import *
import math

def Leftclick(event):
    ans = float(textboxWeight.get()) / math.pow(float(textboxheight.get())/100, 2)
    if ans >= 30:
        labelResult.configure(text="อ้วนมาก!!")
    elif ans >= 25:
        labelResult.configure(text="อ้วน!")
    elif ans >= 23:
        labelResult.configure(text="น้ำหนักเกิน")
    elif ans >= 18.6:
        labelResult.configure(text="ปกตื :)")
    else:
        labelResult.configure(text="ผอมเกินไป")
    NumberResult.configure(text=float(textboxWeight.get()) / math.pow(float(textboxheight.get())/100, 2))
def Rightclick(event):
    print("Right")
def Doubleclick(event):
    print("Double")
main = Tk()

labelheight = Label(main, text='Height(เซนติเมตร):')
labelheight.grid(row=0, column=0)
textboxheight = Entry(main)
textboxheight.grid(row=0,column=1)

labelweight = Label(main, text='Weight(กิโลกรัม):')
labelweight.grid(row=1, column=0)
textboxWeight = Entry(main)
textboxWeight.grid(row=1, column=1)

Calculate = Button(main, text='คำนวณ')
Calculate.grid(row=2)
Calculate.bind('<Button-1>', Leftclick)

labelResult = Label(main, text='ระดับสุขภาพ')
labelResult.grid(row=2, column=1)

NumberResult = Label(main, text='ผลลัพธ์ตัวเลข')
NumberResult.grid(row=3, column=1)

main.mainloop()