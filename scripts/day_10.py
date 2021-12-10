#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from itertools import pairwise


def load_nav_lines(file):
    with open(file) as f:
        nav_lines = f.readlines()
        nav_lines = [line.strip() for line in nav_lines]
    return nav_lines


def get_illegal_character(line):
    valid_pairs = ["()", "{}", "[]", "<>"]
    temp = line
    while any([pair in temp for pair in valid_pairs]):
        for pair in valid_pairs:
            temp = temp.replace(pair, "")
    if not any([x in "}]>)" for x in temp]):
        return "Incomplete"
    else:
        for a, b in pairwise(temp):
            if b in "}]>)":
                return b


def get_incomplete_line(line):
    valid_pairs = ["()", "{}", "[]", "<>"]
    temp = line
    while any([pair in temp for pair in valid_pairs]):
        for pair in valid_pairs:
            temp = temp.replace(pair, "")
    if not any([x in "}]>)" for x in temp]):
        return temp
    return "Illegal"


def part_one(nav_lines):
    results = [get_illegal_character(line) for line in nav_lines]
    illegal = [x for x in results if x != "Incomplete"]
    scoring_map = {")": 3, "]": 57, "}": 1197, ">": 25137}
    scores = [scoring_map[x] for x in illegal]
    final_score = sum(scores)
    return final_score


def score_closer(closer):
    scoring_map = {")": 1, "]": 2, "}": 3, ">": 4}
    score = 0
    for x in closer:
        score = score * 5
        score += scoring_map[x]
    return score


def part_two(nav_lines):
    swap_map = {"{": "}", "(": ")", "<": ">", "[": "]"}
    results = [get_incomplete_line(line) for line in nav_lines]
    incompletes = [x for x in results if x != "Illegal"]
    closers = ["".join([swap_map[i] for i in x])[::-1] for x in incompletes]
    scores = [score_closer(c) for c in closers]
    scores = sorted(scores)
    med_idx = int(len(scores) / 2)
    final_score = scores[med_idx]
    return final_score

if __name__ == "__main__":
    nav_lines = load_nav_lines("../data/10_input.txt")
    print(part_one(nav_lines))
    print(part_two(nav_lines))
