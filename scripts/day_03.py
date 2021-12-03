#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from collections import Counter


def load_diagnostic_matrix(file):
    with open(file) as f:
        report = f.readlines()
    report = [(x.replace("\n", "")) for x in report]
    return report


def get_column(matrix, index):
    """
    :param matrix: a list of iterables of the same length
    :param index: zero-indexed column to select
    :returns: column as string
    """
    column = "".join([x[index] for x in matrix])
    return column


def get_power_consumption(matrix):
    """
    :param matrix: a list of iterables of the same length
    :returns: power consumption as int
    """
    columns = [get_column(matrix, i) for i in range(len(matrix[0]))]

    gamma_binary = "".join([Counter(col).most_common()[0][0] for col in columns])
    epsilon_binary = "".join([Counter(col).most_common()[-1][0] for col in columns])
    power_consumption = int(gamma_binary, 2) * int(epsilon_binary, 2)
    return power_consumption


def get_most_common(col):
    counter = Counter(col)
    if counter["1"] >= counter["0"]:
        return "1"
    else:
        return "0"


def get_least_common(col):
    counter = Counter(col)
    if counter["1"] < counter["0"]:
        return "1"
    else:
        return "0"


def get_og_rating(matrix):
    temp_matrix = matrix
    for i in range(len(matrix[0])):
        col = get_column(temp_matrix, i)
        keeper = get_most_common(col)
        temp_matrix = [row for row in temp_matrix if row[i] == keeper]
        if len(temp_matrix) == 1:
            return temp_matrix[0]
    return temp_matrix


def get_cs_rating(matrix):
    temp_matrix = matrix
    for i in range(len(matrix[0])):
        col = get_column(temp_matrix, i)
        keeper = get_least_common(col)
        temp_matrix = [row for row in temp_matrix if row[i] == keeper]
        if len(temp_matrix) == 1:
            return temp_matrix[0]
    return temp_matrix


def part_one():
    matrix = load_diagnostic_matrix("../data/03_input.txt")
    power_consumption = get_power_consumption(matrix)
    print(power_consumption)


def part_two():
    matrix = load_diagnostic_matrix("../data/03_input.txt")
    og_decimal = int(get_og_rating(matrix), 2)
    cs_decimal = int(get_cs_rating(matrix), 2)
    life_support = og_decimal * cs_decimal
    print(life_support)


if __name__ == "__main__":
    part_one()
    part_two()
