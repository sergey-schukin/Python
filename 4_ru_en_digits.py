# Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Напишите программу, открывающую файл на чтение и считывающую построчно данные. При
# этом английские числительные должны заменяться на русские. Новый блок строк должен
# записываться в новый текстовый файл.


vocab = {
    'One': 'Один',
    'Two': 'Два',
    'Three': 'Три',
    'Four': 'Четыре'}

try:
    with open('hw_5_4_a.txt', encoding='utf-8') as f_obj_1:
        f_data = [line.strip('\n').split(' - ') for line in f_obj_1]
        for el in f_data:
            # заменяем английские цифры на русские, используя словарь
            el[0] = vocab[el[0]]
        try:
            with open('hw_5_4_b.txt', 'w', encoding='utf-8') as f_obj_2:
                for el in f_data:
                    print(f'{el[0]} - {el[1]}', file=f_obj_2)
        except IOError:
            print("Произошла ошибка записи файла!")
except IOError:
    print("Произошла ошибка чтения файла!")



