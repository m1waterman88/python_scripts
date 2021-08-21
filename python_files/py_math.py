from math import prod
from random import randrange
from statistics import mean, median, mode

n = 0
num_list = []

while n < 16:
    num_list.append(randrange(1, 56))
    n += 1

length = len(num_list)
min = min(num_list)
max = max(num_list)
mean = mean(num_list)
median = median(num_list)
mode = mode(num_list)
sum = sum(num_list)
product = prod(num_list)

print()
print(f'{num_list= }'.replace('=', ':'))
print(f'{length= }'.replace('=', ':'))
print(f'{min= }'.replace('=', ':'))
print(f'{max= }'.replace('=', ':'))
print(f'{mean= }'.replace('=', ':'))
print(f'{median= }'.replace('=', ':'))
print(f'{mode= }'.replace('=', ':'))
print(f'{sum= }'.replace('=', ':'))
print(f'{product= }'.replace('=', ':'))
print()


'''
# min without min()
min = sorted(num_list)[0]

# max without max()
max = sorted(num_list)[-1]

# mean without mean()
sum(num_list)/len(num_list)

# sum without sum()
i = 0
sum = 0
while i < len(num_list):
    sum += num_list[i]
    i += 1

# product without math.prod()
j = 0
product = 1
while j < len(num_list):
    product *= num_list[j]
    j += 1
'''
