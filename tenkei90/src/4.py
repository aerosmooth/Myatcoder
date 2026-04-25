import sys


def solve():
    tokens = list(map(int, sys.stdin.read().split()))
    height, width = tokens[0], tokens[1]

    grid = []
    for row_index in range(height):
        start = 2 + row_index * width
        grid.append(tokens[start : start + width])

    row_sums = [sum(row) for row in grid]
    col_sums = [
        sum(grid[row_index][col_index] for row_index in range(height))
        for col_index in range(width)
    ]

    for row_index in range(height):
        for col_index in range(width):
            print(
                row_sums[row_index] + col_sums[col_index] - grid[row_index][col_index],
                end=" ",
            )
        print()


if __name__ == "__main__":
    solve()
