# 2. Создать текстовый файл (не программно), сохранить в нём несколько строк, выполнить
# подсчёт строк и слов в каждой строке.

try:
    with open('hw_5_2.txt', encoding='utf-8') as f_obj:
        content = f_obj.read().splitlines()
        print(f'Количество строк в файле: {len(content)}')
        for line in content:
            print(f'Строка {content.index(line)+1}. Длина: {len(line)}; Значение: {line}')
except IOError:
    print("Произошла ошибка чтения файла!")
