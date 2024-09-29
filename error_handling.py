
#################### Python reported the Error
# ValueError: invalid literal for int() with base 10: '1a'
#x: int = int('1a')

# IndexError: list index out of range
#                   0   1   2  3  4
#list1: list[int] = [8, -2, 19]
#print(list1[3])

# TypeError: unsupported operand type(s) for +=: 'NoneType' and 'int'
#x: int = None
#x += 1

# ZeroDivisionError: division by zero
# 2 / 0

###################### I created the error
# AttributeError: the height {5.0} is not acceptable.
height: float = float(input('Tell me your height: '))
if not 1.40 <= height <= 2.80:
    raise AttributeError(f"the height {height} is not acceptable.")
print(f"height {height:.2f} is ok.")




