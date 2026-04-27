import sys


def read_input():
    input_data = sys.stdin.read().split()
    N = int(input_data[0])
    K = int(input_data[1])
    A = [int(x) for x in input_data[2 : 2 + N]]
    B = [int(x) for x in input_data[2 + N : 2 + 2 * N]]

    return N, K, A, B


def solve():
    N, K, A, B = read_input()
    diff_AB = [0] * N
    for i in range(N):
        diff_AB[i] = abs(A[i] - B[i])

    if (K - sum(diff_AB)) >= 0 and (K - sum(diff_AB)) % 2 == 0:
        print("Yes")
    else:
        print("No")


if __name__ == "__main__":
    solve()
