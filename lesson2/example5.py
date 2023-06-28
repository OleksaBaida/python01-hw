try:
    x = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero!")
except ValueError:
    print("Invalid value!")
except Exception as e:
    print("An error occurred:", str(e))

