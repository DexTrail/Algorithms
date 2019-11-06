# -*- coding: utf-8 -*-


def sort(*args, key=lambda x: x, reverse: bool = False, counter: list = [0]) -> list:
    """
    Сортировка слиянием.

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

    def mergesort(arr):
        nonlocal key
        if len(arr) < 2:
            return arr

        middle = len(arr) // 2
        arr1, arr2 = mergesort(arr[:middle]), mergesort(arr[middle:])
        idx1, idx2 = 0, 0
        res = []
        while idx1 < len(arr1) and idx2 < len(arr2):
            counter[0] += 1
            if not reverse:
                if key(arr1[idx1]) <= key(arr2[idx2]):
                    res += [arr1[idx1]]
                    idx1 += 1
                else:
                    res += [arr2[idx2]]
                    idx2 += 1
            else:
                if key(arr1[idx1]) >= key(arr2[idx2]):
                    res += [arr1[idx1]]
                    idx1 += 1
                else:
                    res += [arr2[idx2]]
                    idx2 += 1
        res += arr1[idx1:] + arr2[idx2:]

        return res

    return mergesort(arr)
