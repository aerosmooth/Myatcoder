import sys


def read_input():
    input_data = sys.stdin.read().split()

    N = int(input_data[0])
    P = int(input_data[1])
    Q = int(input_data[2])

    A = [int(x) % P for x in input_data[3 : 3 + N]]

    return N, P, Q, A


def solve():
    N, P, Q, A = read_input()
    count = 0
    for i in range(N):
        for j in range(i + 1, N):
            for k in range(j + 1, N):
                for l in range(k + 1, N):
                    for m in range(l + 1, N):
                        if (A[i] * A[j] * A[k] * A[l] * A[m]) % P == Q:
                            count += 1

    print(count)


if __name__ == "__main__":
    solve()
