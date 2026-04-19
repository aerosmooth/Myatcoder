import sys


def solve():
    input_data = sys.stdin.read().split()
    N = int(input_data[0])
    X = int(input_data[1])
    Y = int(input_data[2])
    A = []
    for i in range(N):
        A.append(int(input_data[3 + i]))


if __name__ == "__main__":
    solve()
