import sys


def solve():
    input_data = sys.stdin.read().split()
    N = int(input_data[0])
    S = input_data[1]
    print(S.lstrip("o"))


if __name__ == "__main__":
    solve()
