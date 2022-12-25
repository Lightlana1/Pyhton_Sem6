# Напишите программу, удаляющую из текста все слова, содержащие ""абв"".
# c использованием lambda и filter
with open('file2.txt', 'w') as data:
    data.write('абв где абвуке орп эюя')

with open('file2.txt', 'r') as data:
    str = data.readline()

x = 'абв'
str2 = str.split()
filter_str = ' '.join((filter(lambda s: x not in s, str2)))
print(filter_str)

with open('file2.txt', 'a') as file:
     file.write('\n' + filter_str)
