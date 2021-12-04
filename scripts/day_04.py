#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from dataclasses import dataclass, field
from typing import List


@dataclass
class Bingo:
    """Class representing a single bingo board."""

    board: str
    draws: List = field(default_factory=lambda: [])
    marks: List = field(
        default_factory=lambda: [[False for i in range(5)] for j in range(5)]
    )
    moves: int = 0
    score: int = 0
    win: bool = False

    def gen_matrix(self):
        if self.board.endswith("\n"):
            self.board = self.board[:-2]
        board_list = self.board.split("\n")
        matrix_str = [row.split() for row in board_list]
        matrix_final = [[int(v) for v in r] for r in matrix_str]
        self.matrix = matrix_final

    def __post_init__(self):
        self.gen_matrix()

    def get_score(self):
        last_draw = self.draws[-1]
        unmarked = []
        for mrow, brow in zip(self.marks, self.matrix):
            for i in range(5):
                if mrow[i] == False:
                    unmarked.append(brow[i])
        score = last_draw * sum(unmarked)
        self.score = score

    def check_win(self):
        sums = []
        cols = [[row[i] for row in self.marks] for i in range(5)]
        for row in self.marks:
            sums.append(sum(row))
        for col in cols:
            sums.append(sum(col))
        if any([s == 5 for s in sums]):
            self.win = True
            self.get_score()

    def move(self, draw):
        if self.win == True:
            return
        self.draws.append(draw)
        self.moves += 1
        temp_marks = []
        for row in self.matrix:
            temp_row = [x in self.draws for x in row]
            temp_marks.append(temp_row)
        self.marks = temp_marks
        pprint(self.marks)
        self.check_win()


def load_draws_boards(file):
    with open(file) as f:
        report = f.read()
    report = report.split("\n\n")
    draws = [int(d) for d in report[0].split(",")]
    return draws, report[1:]


def parts_one_and_two():
    draws, boards = load_draws_boards("../data/04_input.txt")

    bingos = [Bingo(board) for board in boards]

    for draw in draws:
        for bingo in bingos:
            bingo.move(draw)

    fewest_moves = min([b.moves for b in bingos])
    most_moves = max([b.moves for b in bingos])

    for i, b in enumerate(bingos):
        if b.moves == fewest_moves:
            print(f"Fewest moves: {b.moves}. Score: {b.score}. Board #{i+1}")
        if b.moves == most_moves:
            print(f"Most moves: {b.moves}. Score: {b.score}. Board #{i+1}")


if __name__ == "__main__":
    parts_one_and_two()
