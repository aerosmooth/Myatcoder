import sys


def solve():
    input_data = sys.stdin.read().split()
    N = int(input_data[0])
    M = int(input_data[1])
    A = [[0] * N] * M
    for i in range(M):
        for j in range(N):
            A[i][j] = int(input_data[1 + i * M + j])


if __name__ == "__main__":
    solve()
