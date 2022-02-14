# Вводятся три разных числа. Найти, какое из них является средним (больше одного, но меньше другого).

def middle_value():
    a, b, c = map(int, input('введите три числа').split())
    if b < a < c or c < a < b:
        return f'Среднее число {a}'
    elif a < b < c or c < b < a:
        return f'Среднее число {b}'
    else:
        return f'Среднее число {c}'


print(middle_value())
