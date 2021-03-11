# 6. Реализовать функцию int_func(), принимающую слово из маленьких латинских букв и возвращающую его же,
# но с прописной первой буквой. Например, print(int_func(‘text’)) -> Text.
# Продолжить работу над заданием. В программу должна попадать строка из слов, разделенных пробелом.
# Каждое слово состоит из латинских букв в нижнем регистре. Сделать вывод исходной строки,
# но каждое слово должно начинаться с заглавной буквы. Необходимо использовать написанную ранее функцию int_func().

def check_input_word(input_word):
    '''Возвращает True, если введенное слово состоит только из маленьких латинских букв'''
    for letter in list(input_word):
        if letter == '':
            pass
        elif ord(letter) not in range(ord('a'), ord('z')+1):
            return False
    return True


def int_func_single(error_msg, word):
    '''возвращает слово с заглавной буквы'''
    if check_input_word(word):
        return word.capitalize()
    else:
        return error_msg


def int_func_multi(error_msg, *args):
    '''возвращает слова с заглавной буквы'''
    res = ''
    for arg in args:
        if check_input_word(arg):
            res += f'{arg.capitalize()} '
        else:
            return error_msg
    return res


error_msg = 'Некорректный ввод данных'
print(int_func_single(error_msg, input('Введите слово из маленьких латинских букв: ')))
print(int_func_multi(error_msg, *input('Введите слова из маленьких латинских букв: ').split(' ')))
