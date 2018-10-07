#!/usr/bin/python2
# -*- coding: utf-8 -*-

#THIS IS NOT OPTIMAL SOLUTION!
#I USED THIS CODE AS AN EXAMPLE OF ACTION ON LISTS AND DICTIONARIES IN PYTHON.


import collections

def change_to_roman(fun_component, fun_position, fun_multiplier):
    roman = collections.OrderedDict()
    roman["I"] = 1
    roman["V"] = 5
    roman["X"] = 10
    roman["L"] = 50
    roman["C"] = 100
    roman["D"] = 500
    roman["M"] = 1000

    if int(fun_component) * fun_multiplier in roman.values():
        return (roman.keys()[roman.values().index(int(fun_component) * fun_multiplier)])

    for addend in [0, 1]:

        if roman[roman.keys()[fun_position + addend]] <= int(fun_component) * fun_multiplier < roman[
            roman.keys()[fun_position + addend + 1]]:

            if roman[roman.keys()[fun_position + addend + 1]] - roman[roman.keys()[fun_position]] == int(
                    fun_component) * fun_multiplier:

                return (str(roman.keys()[fun_position]) + str(roman.keys()[fun_position + addend + 1]))


            else:

                if addend == 0:
                    return (str(roman.keys()[fun_position]) * int(fun_component))

                if addend == 1:
                    return (str(roman.keys()[fun_position + addend]) + (
                        str(roman.keys()[fun_position]) * (
                            int(fun_component) - roman[roman.keys()[fun_position + addend]] / fun_multiplier)))


def number_to_roman(number):
    answer = []
    position = 0
    multiplier = 1

    for component in reversed(list(str(number % 1000))):

        if int(component) == 0:
            position += 2
            multiplier *= 10
            continue

        answer.append(change_to_roman(component, position, multiplier))

        position += 2
        multiplier *= 10
    answer.extend(["M"] * (number / 1000))
    return "".join(reversed(answer))


for i in xrange(100001):
    print i,number_to_roman(i)
