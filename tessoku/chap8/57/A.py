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
    LEVELS = 30
    dp = [[None] * N for i in range(LEVELS)]
    for i in range(N):
        dp[0][i] = A[i] - 1

    for d in range(1, LEVELS):
        for i in range(N):
            dp[d][i] = dp[d - 1][dp[d - 1][i]]

    for i in range(Q):
        x = X[i]
        y = Y[i]
        current_place = x - 1
        for i in range(LEVELS - 1, -1, -1):
            if ((y >> i) & 1) == 1:
                current_place = dp[i][current_place]

        print(current_place + 1)


if __name__ == "__main__":
    solve()
