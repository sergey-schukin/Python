# создаем функцию для проверки введенных пользователем чисел
# дистанция должна быть положительным числом
# аргумент функции - это текст, чтобы указать пользователю какой именно показатель нужно ввести
def input_number(dist_type):
    while True:
        try:
            distance = float(input(f'Пожалуйста, введите {dist_type}: '))
            if distance < 0:
                print('Дистанция должна быть больше 0. Пожалуйста, повторите ввод.')
                continue
            return distance
            # break
        except ValueError:
            print("Это не число. Пожалуйста, повторите ввод.")


current_dist = input_number('результат в первый день пробежки (в км)')
target_dist = input_number('целевую дистанцию для пробежки (в км)')
day_count = 0  # счетчик дней
# создаем цикл. на каждом шагу прибавляем 1 день и прибавляем 10% дистанции относительно предыдущего дня
while True:
    day_count += 1
    print(f'{day_count}-й день: {current_dist:.2f}')
    if current_dist >= target_dist:
        print(f'Ответ: на {day_count}-й день спортсмен достиг результата — не менее {target_dist} км.')
        break
    current_dist *= 1.1
