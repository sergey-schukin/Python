# 2. Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя:
# имя, фамилия, год рождения, город проживания, email, телефон.
# Функция должна принимать параметры как именованные аргументы.
# Реализовать вывод данных о пользователе одной строкой.

def my_func(name, surname, year, city, email, telephone):
    '''Возвращает данные пользователя одной строкой.'''
    return ' '.join([name, surname, year, city, email, telephone])


print(my_func(surname='Smith', name='John', year='1988', city='Moscow', email='JSmith@gmail.com',
              telephone='+7-999-999-99-99'))
