#!/usr/bin/env python
# -*- coding=utf-8 -*-

"""
Regras do Fizzbuzz

1. Se a posição for múltiplo de 3: fizz
2. Se a posição for múltiplo de 5: buzz
3. Se a posição for múltimplo de 3 e 5: fizzbuzz
4. Para qualquer outra posição fale o próprio número.
"""
def multiple_of(base, num):
    return num%base == 0


def robot(pos):
    say = str(pos)
    if multiple_of(3, pos) and multiple_of(5, pos):
        say = 'fizzbuzz'
    elif multiple_of(3, pos):
        say = 'fizz'
    elif multiple_of(5, pos):
        say = 'buzz'
    return say

