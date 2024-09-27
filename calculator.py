from tkinter import *


window = Tk()


# Screen settings
window.title("Calculator")
window.minsize(width=300, height=400)


# Calculator elements
calculator_display = Text(window, height=2, width=16, font=("Arial", 20))
calculator_display.grid(row=0, column=0, columnspan=4)

button9 = Button(text="9", height=2, width=4)
button9.grid(row=1, column=0)

button8 = Button(text="8", height=2, width=4)
button8.grid(row=1, column=1)

button7 = Button(text="7", height=2, width=4)
button7.grid(row=1, column=2)

button6 = Button(text="6", height=2, width=4)
button6.grid(row=2, column=0)

button5 = Button(text="5", height=2, width=4)
button5.grid(row=2, column=1)

button4 = Button(text="4", height=2, width=4)
button4.grid(row=2, column=2)

button3 = Button(text="3", height=2, width=4)
button3.grid(row=3, column=0)

button2 = Button(text="2", height=2, width=4)
button2.grid(row=3, column=1)

button1 = Button(text="1", height=2, width=4)
button1.grid(row=3, column=2)

button0 = Button(text="0", height=2, width=4)
button0.grid(row=4, column=1)

button_clear = Button(text="C", height=2, width=4)
button_clear.grid(row=1, column=3)

button_plus = Button(text="+", height=2, width=4)
button_plus.grid(row=2, column=3)

button_minus = Button(text="-", height=2, width=4)
button_minus.grid(row=3, column=3)

button_multiply = Button(text="*", height=2, width=4)
button_multiply.grid(row=4, column=3)

button_divide = Button(text="/", height=2, width=4)
button_divide.grid(row=4, column=2)

button_equals = Button(text="=", height=2, width=4)
button_equals.grid(row=4, column=0)


window.mainloop()
