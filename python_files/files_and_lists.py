# _*_ coding: utf-8 _*_

filepath = 'C:\\Users\\m1wat\\OneDrive\\Desktop\\MindTap - Cengage Learning.pdf'
file = list(open(filepath, 'rb').read()[400:600])

'''
# use a loop
i = 0
for i in range(len(file)):
    print(file[i])
    i += 1
'''

# use map() and join()
# print('\n'.join(map(str, file)))

# use * and separator
print(*file, sep='\n')
