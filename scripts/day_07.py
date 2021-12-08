#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from collections import Counter


def load_crabs(filename):
    with open(filename) as f:
        temp = f.read().strip()
    crabs = [int(x) for x in temp.split(",")]
    return crabs


def part_one(crabs):
    positions = Counter(crabs)
    min_position = min(positions.keys())
    max_position = max(positions.keys())
    fuel_costs = {}
    for i in range(min_position, max_position):
        cost = sum([abs(pos - i) * count for pos, count in positions.items()])
        fuel_costs[i] = cost

    return min(fuel_costs.values())


def part_two(crabs):
    positions = Counter(crabs)
    min_position = min(positions.keys())
    max_position = max(positions.keys()) + 1
    fuel_costs = {}
    for i in range(min_position, max_position):
        cost = sum(
            [sum(range(abs(pos - i) + 1)) * count for pos, count in positions.items()]
        )
        fuel_costs[i] = cost

    return min(fuel_costs.values())


if __name__ == "__main__":
    crabs = load_crabs("../data/07_input.txt")
    print(part_one(crabs))
    print(part_two(crabs))