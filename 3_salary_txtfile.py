# Создать текстовый файл (не программно). Построчно записать фамилии сотрудников и
# величину их окладов (не менее 10 строк). Определить, кто из сотрудников имеет оклад менее
# 20 тысяч, вывести фамилии этих сотрудников. Выполнить подсчёт средней величины дохода сотрудников.

import statistics as st
try:
    with open('hw_5_3.txt', encoding='utf-8') as f_obj:
        salary_list = [line.split() for line in f_obj]
        try:
            # список сотрудников с окладом менее 20000
            list_below_20k = [last_name[0] for last_name in salary_list if float(last_name[1]) < 20000]
        except ValueError:
            print('Ошибка. Введено нечисловое значение зарплаты.')
            raise IOError
        print(f'Список сотрудников с окладом менее 20000 руб.: {list_below_20k}')
        avg_income = st.mean([float(last_name[1]) for last_name in salary_list])
        print(f'Средняя величина дохода сотрудников: {avg_income:.2f}')
except IOError:
    print("Произошла ошибка чтения файла!")
