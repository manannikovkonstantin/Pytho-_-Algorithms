# 1. Найти сумму и произведение цифр трехзначного числа, которое вводит пользователь.


def sum_product_num():
    num = input('введите число ')
    sum_num = 0
    prod_num = 1
    if num.isdigit():
        if len(num) == 3:
            for i in num:
                sum_num += int(i)
                prod_num = prod_num * int(i)
            return f'сумма цифр трехзначного числа {num} = {sum_num} и ' \
                   f'произведение цифр трехзначного числа {num} =  {prod_num}'
        else:
            return f'написано же "трёхзначное число", введи трёхзначное число!!!'
    else:
        return f'это не число! введи число, кожаный!!!'


print(sum_product_num())
