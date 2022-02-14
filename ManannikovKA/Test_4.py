""" 4. Написать программу, которая генерирует в указанных пользователем границах:
случайное целое число;
случайное вещественное число;
случайный символ.
Для каждого из трех случаев пользователь задает свои границы диапазона. 
Например, если надо получить случайный символ от 'a' до 'f', то вводятся эти символы. 
Программа должна вывести на экран любой символ алфавита от 'a' до 'f' включительно."""

import random


def random_generator():
    a = input('Введите число или символ ')
    b = input('Введите число или символ ')
    if a.isdigit() and b.isdigit():
        a1 = int(a)
        b1 = int(b)
        return random.randint((min(a1, b1)), (max(a1, b1)))
    elif (a.find('.') > 0) and (b.find('.') > 0):
        a3 = float(a)
        b3 = float(b)
        return random.triangular((min(a3, b3)), (max(a3, b3)))
    elif a.isalpha() and b.isalpha():
        if len(a) == 1 == len(b):
            a2 = ord(a)
            b2 = ord(b)
            return chr(random.randint((min(a2, b2)), (max(a2, b2))))
        else:
            return f'символ должен быть один!!!'
    else:
        return f'повторите ввод'


print(random_generator())
