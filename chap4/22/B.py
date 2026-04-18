import sys


def solve():
    input_data = sys.stdin.read().split()
    N = int(input_data[0])
    X = []
    Y = []
    for i in range(N):
        X.append(int(input_data[1 + 2 * i]))
        Y.append(int(input_data[2 + 2 * i]))


if __name__ == "__main__":
    solve()
