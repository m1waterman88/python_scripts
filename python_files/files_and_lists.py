# -*- coding: utf-8 -*-

filepath = "C:\\Users\\m1wat\\OneDrive\\Desktop\\MindTap - Cengage Learning.pdf"
file = list(open(filepath, "rb").read()[400:600])

'''
# use a loop
for i in range(len(file)):
    print(file[i])
'''

# use map() and join()
# print('\n'.join(map(str, file)))

# use * and separator
print(*file, sep="\n")
