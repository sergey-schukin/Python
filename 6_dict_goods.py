# создаем 2 глобальных переменные - словари
# словарь, где ключ - это характеристиками товара, а аргументы: 1-тип данных, 2-ограничение для чисел
dict_params = {
    'название': [str, ''],
    'цена': [float, 'positive'],
    'количество': [int, 'non-negative'],
    'eд': [str, '']}
dict_translate = {
    'positive': 'положительное',
    'non-negative': 'не отрицательное'
}
# словарь с меню пользователя
operations = {
    1: 'добавить',
    2: 'аналитика',
    3: 'выход'}


# функция, которая проверяет вводимые пользователем данные на соответствие нужному типу данных
def check_input_data(input_message, error_message, input_type):
    while True:
        try:
            input_number = input_type(input(input_message))
            return input_number
        except ValueError:
            print(error_message)


# функция, которая позволяет пользователю добавить новый товар
def add_goods(list_goods):
    dict_goods = {}
    for param in (dict_params.keys()):  # цикл по каждой характеристике товара
        message = f'Введите {param}: '
        error_msg = 'Некорректный ввод. Пожалуйста, повторите.'
        # цикл для проверки вводимых пользователем данных на соответствие нужному типу данных
        # и ограничений для числовых значений
        while True:
            param_value = check_input_data(message, error_msg, dict_params[param][0])  # проверка типа данных
            if (  # проверка ограничений для числовых значений
                    (dict_params[param][1] == 'positive' and param_value <= 0) or
                    (dict_params[param][1] == 'non-negative' and param_value < 0)
            ):
                print(f'Значение должно быть {dict_translate[dict_params[param][1]]}. Пожалуйста, повторите ввод.')
                continue
            dict_goods.update({param: param_value})
            break  # выход из цикла, когда все значения введены корректно
    list_goods.append((len(list_goods) + 1, dict_goods))  # добавляем запись в список в товарами


# функция для вывода аналитики по введенным ранее товарам
def analytics_goods(list_goods):
    dict_goods = {}
    analytics_list = []

    # создадим цикл в цикле, чтобы перебрать все товары по каждой характеристике товара
    for param in dict_params:  # цикл по каждой характеристике товара
        for goods_num in range(len(list_goods)):  # цикл по каждому товару
            # в списке аккумулируем значения данной характеристики по каждому товару
            analytics_list.append(list_goods[goods_num][1][param])
        # после окончания внутреннего цикла, мы получаем список со всеми значениями
        # данной характеристики по каждому товару. Теперь добавляем в словарь
        # новую запись: ключ - это характеристика, а аргумент - это полученный список в результате
        # выполнения внутреннего цикла. Команда set используется, чтобы убрать дублирование значений.
        dict_goods.update({param: list(set(analytics_list))})
        # опустошаем список для следующего цикла по новой характеристике
        analytics_list = []
    # вывод словаря на экран:
    for key in dict_goods:
        print(key, ': ', dict_goods[key])


list_goods = []  # список для хранения введенных данных о товаре

# цикл для работы в меню. Выход из цикла только по команде пользователя
while True:
    error_msg = 'Некорректный ввод. Пожалуйста, повторите.'
    # конструкция сообщения для вывода меню пользователя на экран
    message = '\nДоступные команды:\n'
    for i in range(len(operations)):
        message += f'{i + 1} - {operations[i + 1]}'
        message += '\n'
    message += f'Введите номер команды (1-{str(len(operations))}): '

    user_action = check_input_data(message, error_msg, int)  # проверка введенного значения на тип данных
    if user_action not in range(1, len(operations) + 1):  # если команда неверная, то повторно запрашиваем пользователя
        print(error_msg)
        continue
    if user_action == 1:
        print('\nКоманда "Добавить"\n')
        add_goods(list_goods)
        print(*list_goods, sep=',\n')
    elif user_action == 2:
        print('\nКоманда "Аналитика"\n')
        analytics_goods(list_goods)
    elif user_action == 3:
        print('\nКоманда "Выход"')
        print('До свидания!')
        break
