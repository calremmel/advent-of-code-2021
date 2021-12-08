#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from collections import Counter


digits_segments = {
    0: "abcefg",
    1: "cf",
    2: "acdeg",
    3: "acdfg",
    4: "bcdf",
    5: "abdfg",
    6: "abdefg",
    7: "acf",
    8: "abcdefg",
    9: "abcdfg",
}

segments_digits = {"".join(sorted(v)): k for k, v in digits_segments.items()}


def part_one():
    with open("../data/08_input.txt") as f:
        in_outs = f.read().strip()
    in_outs = [x.split(" | ") for x in in_outs.split("\n")]
    outs = [len(x) for pair in in_outs for x in pair[1].split()]
    counts = Counter(outs)
    unique_lengths = [2, 4, 3, 7]
    unique_count = sum([v for k, v in counts.items() if k in unique_lengths])
    return unique_count


def translate_line(line):
    ins, outs = line.split(" | ")
    ins_counts = Counter(ins.replace(" ", ""))

    wire_map = {}

    for i in ins.split():
        if len(i) == 2:
            one = i
        elif len(i) == 4:
            four = i
        elif len(i) == 3:
            seven = i
        elif len(i) == 7:
            eight = i

    for k, v in ins_counts.items():
        if v == 4:
            wire_map["e"] = k
        elif v == 6:
            wire_map["b"] = k
        elif v == 9:
            wire_map["f"] = k

    wire_map["a"] = list(set(seven) - set(one))[0]
    wire_map["c"] = list(set(seven) - set([wire_map[wire] for wire in "af"]))[0]
    wire_map["d"] = list(set(four) - set([wire_map[wire] for wire in "bcf"]))[0]
    wire_map["g"] = list(set(eight) - set([wire_map[wire] for wire in "abcdef"]))[0]

    reverse_wire = {v: k for k, v in wire_map.items()}
    reverse_wire[" "] = " "

    translated_out = "".join([reverse_wire[x] for x in outs])
    digit_keys = ["".join(sorted(x)) for x in translated_out.split()]
    out_digits = int("".join([str(segments_digits[k]) for k in digit_keys]))

    return out_digits


def part_two():
    with open("../data/08_input.txt") as f:
        in_outs = f.read().strip()
    return sum([translate_line(line) for line in in_outs.split("\n")])

if __name__ == "__main__":
    one = part_one()
    two = part_two()
    print(one)
    print(two)