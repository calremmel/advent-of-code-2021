#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from pprint import pprint

dumbos_str = """4438624262
6263251864
2618812434
2134264565
1815131247
2612457325
8585767584
7217134556
2825456563
8248473584"""


def get_surrounding(matrix, x, y):
    surrounding = []
    for i in range(-1, 2):
        for j in range(-1, 2):
            surrounding.append((x + i, y + j))
    surrounding = [x for x in surrounding if not any([i < 0 for i in x])]
    surrounding = [x for x in surrounding if x[0] < len(matrix[0])]
    surrounding = [x for x in surrounding if x[1] < len(matrix)]
    return surrounding


def flash(matrix, x, y):
    idx = get_surrounding(matrix, x, y)
    temp = matrix
    temp[x][y] = "F"
    for i, j in idx:
        if temp[i][j] in ["F", "P"]:
            continue
        elif temp[i][j] < 9:
            temp[i][j] += 1
        elif temp[i][j] == 9:
            temp[i][j] = "P"
    return temp


def step(temp_dumbos):
    count_flashes = 0
    incremented_dumbos = [
        [dumbo + 1 if dumbo != 9 else "P" for dumbo in line] for line in temp_dumbos
    ]
    flashed_dumbos = incremented_dumbos.copy()
    while any([d == "P" for row in flashed_dumbos for d in row]):
        for x in range(len(flashed_dumbos)):
            for y in range(len(flashed_dumbos[0])):
                if flashed_dumbos[x][y] == "P":
                    count_flashes += 1
                    flashed_dumbos = flash(flashed_dumbos, x, y)
    stepped_dumbos = [
        [dumbo if dumbo != "F" else 0 for dumbo in line] for line in flashed_dumbos
    ]
    return stepped_dumbos, count_flashes


def part_one(dumbos_str):
    dumbos = [[int(dumbo) for dumbo in line] for line in dumbos_str.split("\n")]

    total = 0
    for x in range(100):
        dumbos, count = step(dumbos)
        total += count
    return total


def part_two(dumbos_str):
    dumbos = [[int(dumbo) for dumbo in line] for line in dumbos_str.split("\n")]

    total = 0
    steps = 0
    for x in range(1000):
        steps += 1
        dumbos, count = step(dumbos)
        total += count
        if all([d == 0 for row in dumbos for d in row]):
            break
    return steps


if __name__ == "__main__":
    print(part_one(dumbos_str))
    print(part_two(dumbos_str))
