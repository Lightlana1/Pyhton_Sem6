# Напишите программу вычисления арифметического выражения заданного строкой.
# Используйте операции +,-,/,*. приоритет операций стандартный.
# - Добавьте возможность использования скобок, меняющих приоритет операций.
# Например, ( 2 + 4 ) / 3 + 2 * ( 2 + 2 ) + 2 * ( 6 - 3 )

ln_in = input('Введите выражение: ').split()

while len(ln_in) != 1:
    if '(' not in ln_in or ')' not in ln_in: # проверяем есть скобки или нет
        while '*' in ln_in or '/' in ln_in:
            try:
                prod_index = ln_in.index('*')
            except:
                prod_index = 100
            try:
                div_index = ln_in.index('/')
            except:
                div_index = 100

            if prod_index < div_index:
                ln_in[prod_index - 1] = int(ln_in[prod_index - 1]) * int(ln_in[prod_index + 1])
                ln_in.pop(prod_index + 1)
                ln_in.pop(prod_index)
            else:
                ln_in[div_index - 1] = int(ln_in[div_index - 1]) / int(ln_in[div_index + 1])
                ln_in.pop(div_index + 1)
                ln_in.pop(div_index)

        while '+' in ln_in or '-' in ln_in:
            try:
                prod_index = ln_in.index('+')
            except:
                prod_index = 100
            try:
                div_index = ln_in.index('-')
            except:
                div_index = 100

            if prod_index < div_index:
                ln_in[prod_index - 1] = int(ln_in[prod_index - 1]) + int(ln_in[prod_index + 1])
                ln_in.pop(prod_index + 1)
                ln_in.pop(prod_index)
            else:
                ln_in[div_index - 1] = int(ln_in[div_index - 1]) - int(ln_in[div_index + 1])
                ln_in.pop(div_index + 1)
                ln_in.pop(div_index)

    if '(' in ln_in: # если скобки есть
        while '(' in ln_in:
            index = ln_in.index('(')
            if ln_in[index + 2] == '+':
                ln_in[index] = int(ln_in[index + 1]) + int(ln_in[index + 3])
                ln_in.pop(index + 4)
                ln_in.pop(index + 3)
                ln_in.pop(index + 2)
                ln_in.pop(index + 1)
            if ln_in[index + 2] == '-':
                ln_in[index] = int(ln_in[index + 1]) - int(ln_in[index + 3])
                ln_in.pop(index + 4)
                ln_in.pop(index + 3)
                ln_in.pop(index + 2)
                ln_in.pop(index + 1)


        while '*' in ln_in or '/' in ln_in:
            try:
                prod_index = ln_in.index('*')
            except:
                prod_index = 100
            try:
                div_index = ln_in.index('/')
            except:
                div_index = 100

            if prod_index < div_index:
                ln_in[prod_index - 1] = int(ln_in[prod_index - 1]) * int(ln_in[prod_index + 1])
                ln_in.pop(prod_index + 1)
                ln_in.pop(prod_index)
            else:
                ln_in[div_index - 1] = int(ln_in[div_index - 1]) / int(ln_in[div_index + 1])
                ln_in.pop(div_index + 1)
                ln_in.pop(div_index)

        while '+' in ln_in or '-' in ln_in:
            try:
                prod_index = ln_in.index('+')
            except:
                prod_index = 100
            try:
                div_index = ln_in.index('-')
            except:
                div_index = 100

            if prod_index < div_index:
                ln_in[prod_index - 1] = int(ln_in[prod_index - 1]) + int(ln_in[prod_index + 1])
                ln_in.pop(prod_index + 1)
                ln_in.pop(prod_index)
            else:
                ln_in[div_index - 1] = int(ln_in[div_index - 1]) - int(ln_in[div_index + 1])
                ln_in.pop(div_index + 1)
                ln_in.pop(div_index)

print('Результат:', ln_in[0])

