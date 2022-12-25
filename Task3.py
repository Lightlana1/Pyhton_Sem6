# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# использование функции map

num = float(input('Введите число: '))
lst = [str(i) for i in str(num)]
lst.remove('.')
lst.remove('0')
print(lst)
summ = 0
num = list(map(int, lst))
print(num)
for i in range (len(num)):
    summ = summ + num[i]
print(summ)