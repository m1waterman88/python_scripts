"""Convert subnets between binary and decimal."""

type = input('\n' 'Welcome to the type converter!' '\n'
             'Enter the type to convert (int/bin): ').casefold()

if type == 'bin':
    num = input('Enter bin: ').replace(' ', '')
    print('Integer equivalent: ', int(num, 2), '\n')
elif type == 'int':
    num = int(input('Enter int: '))
    num = bin(num)[2:]
    print(f'Binary equivalent: {num[0:4]} {num[4:]}' '\n')
else:
    print("Please select 'bin' or 'int'")
