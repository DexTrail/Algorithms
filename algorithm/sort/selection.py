# -*- coding: utf-8 -*-


def sort(*args, key=lambda x: x, reverse: bool = False, counter: list = [0]) -> list:
    """
    Сортировка выбором.

    :param args: список значений
    :param key: функция, применяемая к каждому значению
    :param reverse: обратный порядок сортировки
    :param counter: количество итераций циклов
    :return: отсортированный список
    """

    # Массив нужен для передачи по ссылке.
    # Переменную нужно обнулять каждый раз.
    counter[0] = 0

    arr = [*args[0]]
    arr_length = len(arr)

    for i in range(arr_length):
        value = key(arr[i])
        index = i
        for j in range(i + 1, arr_length):
            counter[0] += 1
            if not reverse:
                if value > key(arr[j]):
                    value = key(arr[j])
                    index = j
            else:
                if value < key(arr[j]):
                    value = key(arr[j])
                    index = j

        t = arr[i]
        arr[i] = arr[index]
        arr[index] = t

    return arr
