# 3. Реализовать функцию my_func(), которая принимает три позиционных аргумента,
# и возвращает сумму наибольших двух аргументов.

def my_func(arg_1, arg_2, arg_3):
    '''Возвращает сумму наибольших двух аргументов'''
    try:
        # создаем список с введенными числами, сортируем по возрастанию.
        my_list = sorted([arg_1, arg_2, arg_3])
        return float(my_list[-1]) + float(my_list[-2])
    except ValueError:
        print('Ошибка. Необходимо ввести числа')
        return


arg_val_1 = input('Введите первое число: ')
arg_val_2 = input('Введите второе число: ')
arg_val_3 = input('Введите третье число: ')
res = my_func(arg_val_1, arg_val_2, arg_val_3)
if res is not None:
    print(f'Сумма наибольших двух аргументов: {res}')
