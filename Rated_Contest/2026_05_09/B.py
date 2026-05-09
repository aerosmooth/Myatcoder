import sys


def solve():
    input_data = sys.stdin.read().split()
    N = int(input_data[0])
    L = []
    A = []
    start = 1
    for i in range(N):
        L.append(int(input_data[start]))
        start += 1
        x = [int(x) for x in input_data[start : start + L[i]]]
        start += L[i]
        A.append(x)

    X = int(input_data[start])
    start += 1
    Y = int(input_data[start])

    print(A[X - 1][Y - 1])


if __name__ == "__main__":
    solve()
