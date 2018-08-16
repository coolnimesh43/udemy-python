def divide(a, b):
    try:
        return (a / b)
    except ZeroDivisionError:
        return ("You cannot divide a number with 0")
    except NameError:
        return ("The varible is not defined")


def divide_with_condition(a, b):
    return (a / b) if b > 0 else 0


print("executing method divide: ", divide(1, 0))
print("executing method divide_with_condition: ", divide_with_condition(1, 0))
