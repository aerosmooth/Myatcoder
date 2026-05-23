import sys


def solve():
    input_data = sys.stdin.read().split()
    X = int(input_data[0])
    S = "HelloWorld"
    print(S[: X - 1] + S[X:])


if __name__ == "__main__":
    solve()
