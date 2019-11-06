#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Тестирование алгоритмов поиска.
"""

import random
import time
import winsound
import algorithm.search as _search


def beep():
    winsound.Beep(2500, 250)
    time.sleep(.05)
    winsound.Beep(2500, 250)


def print_results(name: str, value, timer: float = 0., counter: list = [0]):
    print("\n{name}\nРезультат ({counter} циклов за {timer:.3} сек. - {ct:.3} сек./цикл): {value}"
          .format(name=name, value=value, counter=counter, timer=timer, ct=timer / counter[0]))


if __name__ == '__main__':
    random.seed(100)
    test_arr = [random.randrange(0, int(100e+6)) for i in range(int(1e+6))]
    searching_val = test_arr[int(9e+5)]
    print("Тестовый массив:")
    print(test_arr)
    print("Искомое значение:", searching_val)

    counter = [0]
    __timer_star = time.perf_counter()
    test_arr.sort()
    value = _search.binary(searching_val, test_arr, counter=counter)
    __timer_end = time.perf_counter()
    print_results("Двоичный поиск - O(log n).", value, __timer_end - __timer_star, counter)

    counter = [0]
    __timer_star = time.perf_counter()
    value = _search.linear(searching_val, test_arr, counter=counter)
    __timer_end = time.perf_counter()
    print_results("Линейный поиск - O(n).", value, __timer_end - __timer_star, counter)

    beep()
