from tkinter import *

root = Tk()
root.title("Calculator")

e = Entry(bg='gray')
e.grid(row=0, column=0, columnspan=3)


def button(number):
    current_numb = e.get()
    e.delete(0, END)
    e.insert(0, str(current_numb) + str(number))


def operator(operator_2):
    global operat
    global first_number

    operat = operator_2
    first_number = e.get()
    e.delete(0, END)


def equal():
    last_number = e.get()
    e.delete(0, END)

    if operat == "button_add":
        e.insert(0, int(first_number) + int(last_number))
    elif operat == "button_subtract":
        e.insert(0, int(first_number) - int(last_number))
    elif operat == "button_multiply":
        e.insert(0, int(first_number) * int(last_number))
    elif operat == "button_divide":
        e.insert(0, int(first_number) / int(last_number))


def clear():
    e.delete(0, END)


button_1 = Button(root, text='1', padx=20, pady=10, command=lambda: button(1))
button_2 = Button(root, text='2', padx=20, pady=10, command=lambda: button(2))
button_3 = Button(root, text='3', padx=20, pady=10, command=lambda: button(3))

button_4 = Button(root, text='4', padx=20, pady=10, command=lambda: button(4))
button_5 = Button(root, text='5', padx=20, pady=10, command=lambda: button(5))
button_6 = Button(root, text='6', padx=20, pady=10, command=lambda: button(6))

button_7 = Button(root, text='7', padx=20, pady=10, command=lambda: button(7))
button_8 = Button(root, text='8', padx=20, pady=10, command=lambda: button(8))
button_9 = Button(root, text='9', padx=20, pady=10, command=lambda: button(9))

button_0 = Button(root, text='0', padx=20, pady=10, command=lambda: button(0))
button_clear = Button(root, text="Clear", padx=40, pady=10, command=clear)

button_add = Button(root, text='+', padx=20, pady=10, command=lambda : operator('button_add'))
button_equal = Button(root, text='=', padx=40, pady=10, command=equal)

button_subtract = Button(root, text='-', padx=20, pady=10, command=lambda: operator('button_subtract'))
button_multiply = Button(root, text='*', padx=20, pady=10, command=lambda: operator('button_multiply'))
button_divide = Button(root, text='/', padx=20, pady=10, command=lambda: operator('button_divide'))

button_1.grid(row=1, column=0)
button_2.grid(row=1, column=1)
button_3.grid(row=1, column=2)

button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)

button_7.grid(row=3, column=0)
button_8.grid(row=3, column=1)
button_9.grid(row=3, column=2)

button_0.grid(row=4, column=0)
button_clear.grid(row=4, column=1, columnspan=2)

button_add.grid(row=5, column=0)
button_equal.grid(row=5, column=1, columnspan=2)

button_subtract.grid(row=6, column=0)
button_multiply.grid(row=6, column=1)
button_divide.grid(row=6, column=2)

root.mainloop()
