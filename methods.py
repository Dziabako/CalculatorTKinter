def evaluate_expression(expression):
    try:
        # Evaluate the expression and return the result
        result = str(eval(expression))
        return result
    except Exception as e:
        return "Error"


def clear_display(display):
    # Clear the display
    display.delete("1.0", "end")