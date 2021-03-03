# создаем функцию для проверки введенных пользователем чисел
# выручка и затраты должны быть положительным числом
# количество сотрудников - должно быть целочисленным положительным числом
# аргументы функции - это:
#   1.текст, чтобы указать пользователю какой именно показатель нужно ввести
#   2. тип переменной (float для выручки и затрат, int для количества сотрудников)

def input_number(fin_indicator, input_type):
    while True:
        try:
            number = input_type(input(f'Пожалуйста, введите показатель {fin_indicator}: '))
            if number <= 0:
                print('Показатель должен быть больше 0. Пожалуйста, повторите ввод.')
                continue
            return number
            break
        except ValueError:
            if input_type == int:
                print('Это не целочисленное значение. Пожалуйста, повторите ввод')
            else:
                print("Это не число. Пожалуйста, повторите ввод.")


income = input_number('выручка', float)
costs = input_number('затраты', float)
fin_result = income - costs
if fin_result > 0:
    print(f"Прибыль: {fin_result:.2f}")
    print(f"Рентабельность: {fin_result / income:.2f}")
    num_employees = input_number('количество сотрудников', int)
    print(f'Прибыль на 1 сотрудника: {fin_result / num_employees:.2f}')
elif fin_result == 0:
    print("Сработали в ноль")
else:
    print(f"Убыток: {fin_result:.2f}")
