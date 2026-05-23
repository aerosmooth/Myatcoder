import sys


def solve():
    input_data = sys.stdin.read().split()
    S = input_data[0]
    N = int(input_data[1])

    print(S[N:-N])


if __name__ == "__main__":
    solve()
