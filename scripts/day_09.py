#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def load_heightmap(file):
    with open(file) as f:
        heightmap = f.read().strip()
    matrix = [[int(i) for i in row] for row in heightmap.split("\n")]
    return matrix


def get_neighbors(matrix, point):
    i, j = point
    neighbors = [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]
    neighbors = [
        (x, y)
        for x, y in neighbors
        if all([x >= 0, x < len(matrix), y >= 0, y < len(matrix[0])])
    ]
    return neighbors


def get_low_points(matrix):
    low_points = []
    for i, row in enumerate(matrix):
        for j, value in enumerate(row):
            neighbors = get_neighbors(matrix, (i, j))
            if all([value < matrix[x][y] for x, y in neighbors]):
                low_points.append((i, j))
    return low_points


def part_one(matrix):
    low_points = get_low_points(matrix)
    low_values = [matrix[x][y] for x, y in low_points]
    sum_risk = sum([p + 1 for p in low_values])
    return sum_risk


def get_basin(matrix, point):
    checked = []
    basin_members = [point]
    while not all([b in checked for b in basin_members]):
        to_check = [b for b in basin_members if b not in checked]
        for p in to_check:
            new_members = get_basin_members(matrix, p)
            checked.append(p)
            basin_members += new_members
    return set(basin_members)


def get_basin_members(matrix, point):
    value = matrix[point[0]][point[1]]
    ns = get_neighbors(matrix, point)
    return [n for n in ns if (matrix[n[0]][n[1]] < 9) & (matrix[n[0]][n[1]] > value)]


def part_two(matrix):
    low_points = get_low_points(matrix)
    basin_sizes = []
    for point in low_points:
        basin_sizes.append(len(get_basin(matrix, point)))

    top_3 = sorted(basin_sizes)[-3:]

    return top_3[0] * top_3[1] * top_3[2]

if __name__ == "__main__":
    matrix = load_heightmap("../data/09_input.txt")
    print(part_one(matrix))
    print(part_two(matrix))