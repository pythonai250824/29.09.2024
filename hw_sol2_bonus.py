
counts: list[int] = []
#          0        1        2     .. 10
#         count0   count1   count2    count10
#numbers = [0,       0,       0, .....  0]
# 1 1 2 2 2
for i in range(11):
    counts.append(0)

SENTINEL: int = -999

while True:
    number = int(input('Enter number:'))
    if number == SENTINEL:
        break
    if not 0 <= number <= 10:
        continue
    counts[number] += 1

    print("Statistics: ", end="")
    for i in range(10 + 1):
        if counts[i]:
            print(f"[ {i} ]: {counts[i]}", end=" ")
    print()