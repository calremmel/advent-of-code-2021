#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from collections import Counter, defaultdict


def load_fish(file):
    with open(file) as f:
        fish = f.read().strip()
    fish = fish.split(",")
    fish = [int(i) for i in fish]
    return fish


def get_num_fish(fish, days):
    counts = Counter(fish)
    while days > 0:
        new_counts = defaultdict(lambda: 0)
        for k, v in counts.items():
            if k == 0:
                new_counts[6] += v
                new_counts[8] += v
            else:
                new_counts[k - 1] += v
        counts = new_counts
        days -= 1

    num_fish = sum(counts.values())
    return num_fish

if __name__ == "__main__":
    fish = load_fish("../data/06_input.txt")
    part_one = get_num_fish(fish, 80)
    print(part_one)
    part_two = get_num_fish(fish, 256)
    print(part_two)
