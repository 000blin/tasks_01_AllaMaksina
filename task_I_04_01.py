# 1. Реализовать скрипт, в котором должна быть предусмотрена функция расчета
# заработной платы сотрудника. В расчете необходимо использовать формулу:
# (выработка в часах * ставка в час) + премия.
# Для выполнения расчета для конкретных значений необходимо запускать скрипт с параметрами.

from sys import argv


def salary(*args):
    """" Функция возвращает з/п работника = кол-во часов(hours) * ставка в час(rate) + премия(bonus)"""
    hours, rate, bonus = args
    return hours * rate + bonus


a = int(argv[1])
b = int(argv[2])
c = int(argv[3])

print(salary(a, b, c))

