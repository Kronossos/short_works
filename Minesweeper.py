#!/usr/bin/python3
# -*- coding: utf-8 -*-
import numpy as np


def check(row, column):
    global game_size
    global game_filed
    points = []
    for x in (-1, 0, 1):
        if row + x not in range(game_size): continue
        for y in (-1, 0, 1):
            if column + y not in range(game_size): continue
            points.append(minesweeper_field[row + x, column + y])
    game_filed[row, column] = points.count(1)

    if game_filed[row, column] == str(0):
        for x in (-1, 0, 1):
            if row + x not in range(game_size): continue
            for y in (-1, 0, 1):
                if column + y not in range(game_size): continue
                if game_filed[row + x, column + y] != str(0):
                    check(row + x, column + y)


print """
HOW TO PLAY?

When game ask you for field just type two numbers (split by comma).

For example:
Chose filed> 3,4

Counting fields starts from 1.

"""

while True:
    try:
        game_size = int(raw_input("Size of game field: "))
        break
    except ValueError:
        print "You have to give an intiger!"

minesweeper_field = np.random.randint(6, size=(game_size, game_size))
for x in np.nditer(minesweeper_field, op_flags=['readwrite']):
    if x > 1: x[...] = 0
game_filed = np.chararray((game_size, game_size))
game_filed[:] = "?"

while True:
    print game_filed

    chosen_field = (raw_input("Chose filed> ")).split(",")
    chosen_field[0] = int(chosen_field[0]) - 1
    chosen_field[1] = int(chosen_field[1]) - 1

    if minesweeper_field[chosen_field[0], chosen_field[1]] == 1:
        print "GAME OVER!"
        print minesweeper_field
        break

    try:
        check(chosen_field[0], chosen_field[1])
    except IndexError:
        print "Wrong input!"

    if str(minesweeper_field).count("1") == str(game_filed).count("?"):
        print "YOU WIN!"
        print minesweeper_field
        break
