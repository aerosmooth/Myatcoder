import sys


def solve():
    input_data = sys.stdin.read().split()
    N = int(input_data[0])
    A = list(map(int, input_data[1 : N + 1]))


if __name__ == "__main__":
    solve()
