#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def load_report(file):
    with open(file) as f:
        report = f.readlines()
        report = [int(x.replace("\n", "")) for x in report]
    return report


def count_increases(report):
    return sum([1 if (x - y) > 0 else 0 for x, y in zip(report[1:], report[:-1])])


def rolling_window(iterable, size):
    """
    :param iterable: the iterable over which to make windows
    :param size: length of desired windows
    :returns: an iterable containing rolling windows
    """
    iter_length = len(iterable)
    return [iterable[x : x + size] for x in range(iter_length - size + 1)]


def part_one():
    report = load_report("../data/01_input.txt")
    increases = count_increases(report)
    print(increases)


def part_two():
    report = load_report("../data/01_input.txt")
    windows = rolling_window(report, 3)
    window_sums = [sum(w) for w in windows]
    increases = count_increases(window_sums)
    print(increases)


if __name__ == "__main__":
    part_one()
    part_two()
