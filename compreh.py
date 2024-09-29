import random

n_list: list[int] = []
for i in range(11):
    n_list.append(i)

#                                right -->        take left <--    remove :
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
list_even: list[int] = [i for i in range(2, 20 + 2, 2)]
print(list_even)

# create a list of numbers 99, 96, 93, ...60
list_99_60: list[int] = [i for i in range(99, 60 - 3, -3)]
print(list_99_60)

# *Bonus: create a list of 10 random numbers between 1-100
list_random: list[int] = [random.randint(1, 100) for _ in range(10)]
print(list_random)

# insert 3 numbers from the user
#numbers_user: list[int] = [int(input('enter number')) for _ in range(3)]
#print(numbers_user)

num_user: list[int] = []
for _ in range(3):
    #num: int = int(input('Enter number: '))
    #num_user.append(num)
    #num_user.append(int(input('Enter number: ')))
    pass

#numbers_user: list[int] = [int(input('enter number')) for _ in range(3)]

# input number from the user
# list from 1-20 only numbers different than the input
# 3
# [1 2 4 5 6 7 8 ... 20]
# num_user: int = int(input('enter number'))
# list_num: list[int] = []
# for i in range(1, 20 + 1):
#     if i != num_user:
#         list_num.append(i)
#                           append , for, if ...
#num: int = int(input('enter number::'))
#list_num_comp: list[int] = [i for i in range(1, 20 + 1) if i != num]
#print(list_num_comp)

# a. create a list of 10 random numbers between -50 to +50
list_random_50: list[int] = [random.randint(-50, +50) for _ in range(10)]
print('list_random_50', list_random_50)
# b. create a list from the list you created in a-> only with the even numbers
only_even: list[int] = []
for number in list_random_50:
    if number % 2 == 0:
        only_even.append(number)
#                        append, for, if
only_even: list[int] = [number for number in list_random_50 if number % 2 == 0]
print('only_even', only_even)

# c. create a list from the list you created in a-> only with positive numbers
only_positive: list[int] = []
for number in list_random_50:
    if number > 0:
        only_positive.append(number)
#                        append, for, if
only_positive: list[int] = [number for number in list_random_50 if number > 0]
print('only_positive', only_positive)

# input a sentence , remove all spaces
sentence: str = input('give me a sentence?')
without_spaces: list[str] = []
for letter in sentence:  # 'give me a sentence?'
    if letter != ' ':
        without_spaces.append(letter)
print(without_spaces)
without_spaces: list[str] = [letter for letter in sentence if letter != ' ']






