
n_list: list[int] = []
for i in range(11):
    n_list.append(i)

#                                right -->        take left <--
#n_list_short: list[int] = [for i in range(11): n_list.append(i)]
#                             no need append
#n_list_short: list[int] = [n_list.append(i) for i in range(11)]
n_list_short: list[int] = [i for i in range(11)]
print(n_list_short)

n_list2: list[int] = []
for i in range(11):
    n_list.append(i ** 2)

n_list_short2: list[int] = [i ** 2 for i in range(11)]
print(n_list_short2)

# create a list of even numbers 2, 4, 6, 8 ...20
# create a list of numbers 99, 96, 93, ...60
# *Bonus: create a list of 10 random numbers
