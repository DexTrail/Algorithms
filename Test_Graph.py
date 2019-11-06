#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Тестирование работы с графами.
"""

import time


def main():
    graph = {"книга": {"пластинка": 5, "постер": 0},
             "пластнка": {"бас-гитара": 15, "барабан": 20},
             "постер": {"бас-гитара": 30, "барабан": 35},
             "бас-гитара": {"пианино": 20},
             "барабан": {"пианино": 10}}

    start = "книга"
    target = "пианино"

    inf = float('inf')
    parents = {}
    visited = set()

    current = start
    pass


if __name__ == '__main__':
    __time_start = time.perf_counter()
    main()
    __time_delta = time.perf_counter() - __time_start
    __TIMES = (('d', 24 * 60 * 60), ('h', 60 * 60), ('m', 60), ('input_string', 1))
    __times = ''
    for __idx in range(len(__TIMES) - 1):
        __t, __time_delta = divmod(__time_delta, __TIMES[__idx][1])
        if __t > 0:
            __times += "{} {} ".format(int(__t), __TIMES[__idx][0])
    __times += "{:.3} {}".format(__time_delta, __TIMES[~0][0])
    print("\n[Finished in {}]".format(__times))
