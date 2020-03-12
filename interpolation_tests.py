name = input('What is your name?\n')

print('Hi, %s.' % name)
print('He said his name is %s.' % name)

print('%s is %d.' % ('Mike', 31))


name = 'Mike'
age = 31

print('{} is {}.'.format(name, age))
print('{0} is {1}.'.format(name, age))
print('{1} is {0}.'.format(age, name))
print('{0} is {0}.'.format(name, age))

print(f"{name} is {age}.")
print(f"{name} is '{age - 2}.'")
