# -*- coding: utf-8 -*-


def search(value, *args, counter: list = [0]) -> [int]:
    """
    Линейный поиск.

    :param value: искомое значение
    :param args: список занчений
    :param counter: количество итераций циклов
    :return: номер позиции в списке или None
    """

    # Массив нужен для передачи по ссылке.
    # Переменную нужно обнулять каждый раз.
    counter[0] = 0

    arr = args[0]

    for i in range(len(arr)):
        counter[0] += 1
        if arr[i] == value:
            return i

    return None
