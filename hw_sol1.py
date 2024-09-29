
temperatures: list[float] = []

SENTINEL: int = -999

while True:
    temp = float(input('enter temperature:'))
    if temp == SENTINEL:
        break
    if not -50 <= temp <= 50:
        continue
    temperatures.append(temp)

temperatures.extend([-20.0, 39.1, 18.5])

print(temperatures)
print(f"max= {max(temperatures)} min= {min(temperatures)}")

# long
if 18.5 in temperatures == True:
    print(True)
else:
    print(False)
# short
print(f"18.5 in temperature:? {18.5 in temperatures:}")

print(f"20 appears {temperatures.count(20.0)} time(s)")

sum_list = sum(temperatures)
avg_temp = sum_list / len(temperatures)
print(f"average = {avg_temp:.2f}")

# [-20.0, 39.1, 18.5]
for temperature in temperatures:
    # show soon ....
    ################# ternary #############
    print(f"{'+' if temperature > 0 else ''}{temperature:.2f}C")

print(f"index 39.1C is #{temperatures.index(39.1)}")

if len(temperatures) > 0:
    del temperatures[0]
print(f"after removing [0] {temperatures}")

if len(temperatures) > 0:
    del temperatures[::2]
print(f"after removing even {temperatures}")

if 18.5 in temperatures:
    temperatures.remove(18.5)
print(f"after removing 18.5 {temperatures}")

temp_last: float = temperatures.pop()
print(f"after pop {temperatures}")

clone_temp: list[float] = temperatures.copy()

clone_temp.sort()
print(f"sorted clone {clone_temp}")

clone_temp_again: list[float] = temperatures.copy()
clone_temp_again.sort(reverse=True)
print(f"sorted reverse {clone_temp}")










