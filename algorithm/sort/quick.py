# -*- coding: utf-8 -*-


def sort(*args, key=lambda x: x, reverse: bool = False, counter: list = [0]) -> list:
    """
    Быстрая сортировка.

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

    def quicksort(arr):
        nonlocal key
        counter[0] += 1
        if len(arr) < 2:
            return arr

        pivot = key(arr[len(arr) // 2])  # Если массив будет уже отсортирован, то arr[0] - худший случай
        less = [i for i in arr[1:] if key(i) <= pivot]
        greater = [i for i in arr[1:] if key(i) > pivot]
        if not reverse:
            return quicksort(less) + [arr[0]] + quicksort(greater)
        else:
            return quicksort(greater) + [arr[0]] + quicksort(less)

    return quicksort(arr)
