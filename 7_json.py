# Создать вручную и заполнить несколькими строками текстовый файл, в котором каждая
# строка будет содержать данные о фирме: название, форма собственности, выручка, издержки.
# Пример строки файла: firm_1 ООО 10000 5000.
# Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также
# среднюю прибыль. Если фирма получила убытки, в расчёт средней прибыли её не включать.
# Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а
# также словарь со средней прибылью. Если фирма получила убытки, также добавить её в
# словарь (со значением убытков).
# Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
# Итоговый список сохранить в виде json-объекта в соответствующий файл.
# Пример json-объекта:
# [{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]

import json
try:
    with open('hw_5_7.txt', encoding='utf-8') as f_obj:
        dict_firms = {}
        sum_profit = 0
        sum_profit_loss = 0
        profit_companies = 0
        for line in f_obj:
            firm_list = line.split()  # преобразуем строку в список
            firm = firm_list[0]
            income = float(firm_list[2])
            costs = float(firm_list[3])
            profit_loss = income - costs
            sum_profit_loss += profit_loss
            if profit_loss > 0:  # для расчета средней прибыли без учета убыточных компаний
                sum_profit += profit_loss
                profit_companies += 1
            print(f'Прибыль компании {firm}: {profit_loss}')
            dict_firms.update({firm: profit_loss})
        print(f'Средняя прибыль (без учета убыточных компаний) составляет: {sum_profit / profit_companies}')
        f_obj.seek(0)  # для повторного чтения возвращаем курсор в начало файла
        firms_data = [dict_firms, {'average_profit': sum_profit_loss / len(f_obj.readlines())}]
        print(firms_data)
        try:
            with open("hw_5_7.json", "w", encoding='utf-8') as json_obj:
                json.dump(firms_data, json_obj)
        except IOError:
            print("Произошла ошибка записи файла!")
except IOError:
    print("Произошла ошибка чтения файла!")

