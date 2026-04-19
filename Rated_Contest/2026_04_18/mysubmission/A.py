import sys


def solve():
    input_data = sys.stdin.read().split()
    L = int(input_data[0])
    R = int(input_data[1])
    print(R - L + 1)


if __name__ == "__main__":
    solve()
