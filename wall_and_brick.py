#!/usr/bin/env python
# -*- coding: utf-8 -*-

if __name__ == "__main__":
    a = float(input("Вводи a: "))
    b = float(input("Вводи b: "))
    c = float(input("Вводи c: "))
    x = float(input("Вводи x: "))
    y = float(input("Вводи y: "))

    s = x * y

    if b * c <= s or a * b <= c or a * c <= s:
        print("Кирпич пройдёт")
    else:
        print("Кирпич не пройдёт")
