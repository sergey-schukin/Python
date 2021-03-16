# Создать программный файл в текстовом формате, записать в него построчно данные,
# вводимые пользователем. Об окончании ввода данных будет свидетельствовать пустая строка.

try:
    with open('hw_5_1.txt', 'w', encoding='utf-8') as f_obj:
        while True:
            input_data = input('Введите данные (пустая строка остановит цикл): ')
            if input_data == '':
                break
            else:
                f_obj.write(input_data + '\n')
except IOError:
    print('Ошибка записи в файл.')

