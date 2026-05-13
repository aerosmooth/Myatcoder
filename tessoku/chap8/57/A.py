import sys


def solve():
    input_data = sys.stdin.read().split()
    N = int(input_data[0])
    Q = int(input_data[1])
    A = []
    A = [int(x) for x in input_data[2 : 2 + N]]
    X = []
    Y = []
    for i in range(Q):
        start = 2 + N + 2 * i
        X.append(int(input_data[start]))
        Y.append(int(input_data[start + 1]))

    caves = {}
    caves[1] = 1
    for i in range(1, 1 + N):
        if A[caves[i] - 1] not in caves.values():
            caves[i + 1] = A[caves[i] - 1]

    print(caves)
    for i in range(Q):
        print(caves[Y[i] + caves[X[i]]])


if __name__ == "__main__":
    solve()
