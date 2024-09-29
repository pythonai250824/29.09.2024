
numbers: list[int] = []

SENTINEL: int = -999

while True:
    number = int(input('Enter number:'))
    if number == SENTINEL:
        break
    if not 0 <= number <= 10:
        continue
    numbers.append(number)

    print("Statistics: ", end="")
    for i in range(10 + 1):
        counts: int = numbers.count(i)
        if counts >= 1:
            print(f"[ {i} ]: {counts}", end=" ")
    print()



