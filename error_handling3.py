x: int = 0
y: int = 0

# 2 / 0  # ZeroDivisionError: division by zero
# int('a')  # ValueError: invalid literal for int() with base 10: 'a'
while True:
    try:
        x = int(input('enter mone:'))
        y = int(input('enter mehane:'))
        print(f"{x} / {y} = {x / y:.2f}")
    except ValueError as e:
        print('this is not a valid number')
        print(e)
    except ZeroDivisionError:
        print('cannot divide by zero')
    except Exception:
        print('catch all')
        break


