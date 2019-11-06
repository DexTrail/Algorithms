#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Тестирование алгоритмов сортировки.
"""

import random
import time
import winsound
import algorithm.sort as _sort


def beep():
    winsound.Beep(2500, 250)
    time.sleep(.05)
    winsound.Beep(2500, 250)


def print_results(name: str, value, timer: float = 0., counter: list = [0]):
    print("\n{name}\nРезультат ({counter} циклов за {timer:.3} сек. - {ct:.3} сек./цикл):\n{value}"
          .format(name=name, value=value, counter=counter, timer=timer, ct=timer / counter[0]))


if __name__ == '__main__':
    random.seed(100)
    test_arr = [random.randrange(0, int(100e+4)) for i in range(int(1e+4))]
    # test_arr = {"a": 10, "b": 5, "e": 15, "d": 20, "c": 25}
    # reverse=True, key=lambda x: test_arr[x]
    print("Тестовый массив:")
    print(test_arr)

    counter = [0]
    __timer_star = time.perf_counter()
    sorted_arr = _sort.quick(test_arr, counter=counter)
    __timer_end = time.perf_counter()
    print_results("Быстрая сортировка - O(n log n) / O(n^2).", sorted_arr, __timer_end - __timer_star, counter)

    counter = [0]
    __timer_star = time.perf_counter()
    sorted_arr = _sort.merge(test_arr, counter=counter)
    __timer_end = time.perf_counter()
    print_results("Сортировка слиянием - O(n log n).", sorted_arr, __timer_end - __timer_star, counter)

    counter = [0]
    __timer_star = time.perf_counter()
    sorted_arr = _sort.selection(test_arr, counter=counter)
    __timer_end = time.perf_counter()
    print_results("Сортировка выбором - O(n^2).", sorted_arr, __timer_end - __timer_star, counter)

    beep()
