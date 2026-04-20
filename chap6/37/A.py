import sys


def solve():
    input_data = sys.stdin.read().split()
    N = int(input_data[0])
    M = int(input_data[1])
    B = int(input_data[2])
    A = []
    for i in range(N):
        A.append(int(input_data[3 + i]))
    C = []
    for i in range(M):
        C.append(int(input_data[3 + N + i]))

    print(M * sum(A) + N * sum(C) + N * M * B)


if __name__ == "__main__":
    solve()
