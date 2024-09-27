from tkinter import *
from methods import *

def button_click(value):
    # Insert the value into the calculator display
    calculator_display.insert(END, value)


def button_equals_click():
    # Get the current expression from the display
    expression = calculator_display.get("1.0", "end-1c")
    # Evaluate the expression
    result = evaluate_expression(expression)
    # Clear the display and show the result
    clear_display(calculator_display)
    calculator_display.insert(END, result)


window = Tk()


# Screen settings
window.title("Calculator")
window.minsize(width=300, height=400)


# Calculator elements
calculator_display = Text(window, height=2, width=16, font=("Arial", 20))
calculator_display.grid(row=0, column=0, columnspan=4)


# Create buttons and assign the button_click function
button9 = Button(window, text="9", height=2, width=4, command=lambda: button_click("9"))
button9.grid(row=2, column=0)

button8 = Button(window, text="8", height=2, width=4, command=lambda: button_click("8"))
button8.grid(row=2, column=1)

button7 = Button(window, text="7", height=2, width=4, command=lambda: button_click("7"))
button7.grid(row=2, column=2)

button6 = Button(window, text="6", height=2, width=4, command=lambda: button_click("6"))
button6.grid(row=3, column=0)

button5 = Button(window, text="5", height=2, width=4, command=lambda: button_click("5"))
button5.grid(row=3, column=1)

button4 = Button(window, text="4", height=2, width=4, command=lambda: button_click("4"))
button4.grid(row=3, column=2)

button3 = Button(window, text="3", height=2, width=4, command=lambda: button_click("3"))
button3.grid(row=4, column=0)

button2 = Button(window, text="2", height=2, width=4, command=lambda: button_click("2"))
button2.grid(row=4, column=1)

button1 = Button(window, text="1", height=2, width=4, command=lambda: button_click("1"))
button1.grid(row=4, column=2)

button0 = Button(window, text="0", height=2, width=4, command=lambda: button_click("0"))
button0.grid(row=5, column=1)

buttom_coma = Button(window, text=".", height=2, width=4, command=lambda: button_click("."))
buttom_coma.grid(row=5, column=0)


# Create buttons for operations
button_clear = Button(window, text="C", height=2, width=4, command=lambda: clear_display(calculator_display))
button_clear.grid(row=1, column=2)

button_plus = Button(text="+", height=2, width=4, command=lambda: button_click("+"))
button_plus.grid(row=2, column=3)

button_minus = Button(text="-", height=2, width=4, command=lambda: button_click("-"))
button_minus.grid(row=3, column=3)

button_multiply = Button(text="*", height=2, width=4, command=lambda: button_click("*"))
button_multiply.grid(row=4, column=3)

button_divide = Button(text="/", height=2, width=4, command=lambda: button_click("/"))
button_divide.grid(row=1, column=3)

button_equals = Button(window, text="=", height=2, width=4, command=button_equals_click)
button_equals.grid(row=5, column=3)


window.mainloop()
