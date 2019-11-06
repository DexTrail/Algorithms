# -*- coding: utf-8 -*-


def search(value, *args, counter: list = [0]) -> [int]:
    """
    Двоичный (бинаный) поиск.

    :param value: искомое значение
    :param args: список занчений
    :param counter: количество итераций циклов
    :return: номер позиции в списке или None
    """

    # Массив нужен для передачи по ссылке.
    # Переменную нужно обнулять каждый раз.
    counter[0] = 0

    arr = args[0]

    search_borders = [0, len(arr) - 1]
    while search_borders[0] <= search_borders[1]:
        counter[0] += 1
        median = (search_borders[0] + search_borders[1]) // 2
        if value == arr[median]:
            return median
        elif value < arr[median]:
            search_borders[1] = median - 1
        else:
            search_borders[0] = median + 1

    return None
