# Задайте список из N элементов, заполненных числами из промежутка [-N, N]. Найдите произведение
# элементов на указанных позициях. Позиции хранятся в файле file.txt в одной строке одно число.
# c использование функций map, list comprehension

num = int(input('Введите число: '))
lst = [n for n in range(-num, num+1)]
print(lst)
with open('file.txt', 'w') as file:
     while True:
          data = input('Укажите позиции для вычисления произведения:')
          if data == '':
               break
          file.write(data+'\n')
with open('file.txt', 'r') as file:
     index = list(map(int, file.readlines()))
     print(index)
result = 1
for i in range(len(index)):
     result *= lst[index[i]]
print(result)