import sys


def solve():
    input_data = sys.stdin.read().split()
    N = int(input_data[0])
    A = [int(x) for x in input_data[1 : 1 + N]]
    X = int(input_data[1 + N])
    print(A[X - 1])


if __name__ == "__main__":
    solve()
