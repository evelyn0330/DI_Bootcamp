def my_division():
    try:
        return 5 / 0
    except ZeroDivisionError:
        print("Error!!! You cannot divide a number by zero.")

my_division()