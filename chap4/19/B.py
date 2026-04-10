import sys


def solve():
    input_data = sys.stdin.read().split()
    N = int(input_data[0])
    W = int(input_data[1])
    w = [0] * N
    v = [0] * N
    for i in range(N):
        w[i], v[i] = int(input_data[2 + 2 * i]), int(input_data[3 + 2 * i])

    # dp[i][j]は重さi以下でjまでの品を使った時の最大価値
    dp = [[0 for _ in range(N + 1)] for _ in range(W + 1)]

    for i in range(1, W + 1):
        for j in range(1, N + 1):
            dp[i][j] = max(dp[i][j - 1], dp[i - 1][j])
            if i >= w[j - 1]:
                dp[i][j] = max(dp[i][j], dp[i - w[j - 1]][j - 1] + v[j - 1])
    print(dp[W][N])


if __name__ == "__main__":
    solve()
