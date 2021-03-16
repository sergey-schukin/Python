# Создать (программно) текстовый файл, записать в него программно набор чисел, разделённых
# пробелами. Программа должна подсчитывать сумму чисел в файле и выводить её на экран.

try:
    with open('hw_5_5.txt', 'w+', encoding='utf-8') as f_obj:
        for el in input('Введите числа через пробел: '):
            if el == ' ':
                pass
            elif el.isdigit() is False:
                raise ValueError
            else:
                print(el, end=' ', file=f_obj)
        f_obj.seek(0)
        file_data = f_obj.readline().strip(' ').split(' ')
        file_data = [int(el) for el in file_data]
        print(f'Сумма = {sum(file_data)}')
except IOError:
    print("Произошла ошибка записи файла!")
except ValueError:
    print('Ошибка. Введено нечисловое значение')
