#################### Python reported the Error
from multiprocessing.managers import Value

# ValueError: invalid literal for int() with base 10: '1a'
x: int = 0

while True:
    # 1
    try: # try the danger code
        # 2
        x = int(input('enter a number: '))
        break
    except: # protection net. catches the error.
        # 3
        # do NOT crash
        # there was an ERROR
        # handle the error
        print('the number was NOT ok')

# 1 2 3 4
# 1 2 4

# 4
print(f'after try .. the good number is {x}')

# write a loop that input a float height
# keep on input-ing until the float(input(..)) succeed and height is between 1.4 - 3.0
height: float = 0
while True:
    try:
        height = float(input('enter height: '))
        if not 1.4 <= height <= 3.0:
            print(f'{height} not in range')
            continue
        break
    except:
        print('wrong height number, or range...')

print(f"height is {height}")

height: float = 0
while True:
    try:
        height = float(input('enter height: '))
        if not 1.4 <= height <= 3.0:
             raise ValueError(f'{height} not in range')
        break
    except:
        print('wrong height number, or range...')

print(f"height is {height}")