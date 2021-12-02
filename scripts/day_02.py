#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from dataclasses import dataclass


@dataclass
class SubmarineOne:
    """Class for tracking position of a submarine."""

    horizontal: int
    depth: int

    def move(self, direction, distance):
        if direction == "forward":
            self.horizontal += distance
        elif direction == "down":
            self.depth += distance
        elif direction == "up":
            self.depth -= distance
        else:
            print("Invalid direction")


@dataclass
class SubmarineTwo:
    """Class for tracking position of a submarine."""

    horizontal: int
    depth: int
    aim: int

    def move(self, direction, distance):
        if direction == "forward":
            self.horizontal += distance
            self.depth += self.aim * distance
        elif direction == "down":
            self.aim += distance
        elif direction == "up":
            self.aim -= distance
        else:
            print("Invalid direction")


def load_course(file):
    with open(file) as f:
        report = f.readlines()
    report = [(x.replace("\n", "")) for x in report]
    report = [(x.split(" ")[0], int(x.split(" ")[1])) for x in report]
    return report


def part_one():
    course = load_course("../data/02_input.txt")
    sub = SubmarineOne(0, 0)
    for direction, distance in course:
        sub.move(direction, distance)
    print(sub.horizontal * sub.depth)


def part_two():
    course = load_course("../data/02_input.txt")
    sub = SubmarineTwo(0, 0, 0)
    for direction, distance in course:
        sub.move(direction, distance)
    print(sub.horizontal * sub.depth)


if __name__ == "__main__":
    part_one()
    part_two()
