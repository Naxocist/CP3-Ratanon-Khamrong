from forex_python.converter import CurrencyRates, CurrencyCodes
from tkinter.ttk import *
from tkinter import *

font = ("Angsana New", 20)


def convert_currency(event):
    result_label.config(text=c.convert(input_combobox.get(), convert_combobox.get(),
                        float(amount_textbox.get())),
                        font=font)
    unit_label = Label(main_window, text=d.get_symbol(convert_combobox.get()), fg="dark blue", font=font).grid(row=3, column=3)


main_window = Tk(className="CurrencyConverter")
main_window.geometry("380x200")

currency_list = []
c = CurrencyRates()
d = CurrencyCodes()
for i in c.get_rates('USD'):
    currency_list.append(i)
variable = StringVar(main_window)
variable.set('USD')

input_label = Label(main_window, text="สกุลเงินที่จะแปลง: ", font=font, fg="green")
input_label.grid(row=0, column=1)

input_combobox = Combobox(main_window, values=currency_list, width=25)
input_combobox.grid(row=0, column=2)

convert_label = Label(main_window, text='สกุลเงินที่อยากได้: ', font=font, fg="purple")
convert_label.grid(row=1, column=1)

convert_combobox = Combobox(main_window, values=currency_list, width=25)
convert_combobox.grid(row=1, column=2)

amount_label = Label(main_window, text="จำนวน: ", font=font, fg='grey')
amount_label.grid(row=2, column=1)

amount_textbox = Entry(font=font)
amount_textbox.grid(row=2, column=2)

submit_button = Button(main_window, text='CONVERT', font=font)
submit_button.grid(row=3, column=1)
submit_button.bind("<Button-1>", convert_currency)

result_label = Label(main_window, text="ผลลัพธ์", font=font, fg="RED")
result_label.grid(row=3, column=2)


main_window.mainloop()
