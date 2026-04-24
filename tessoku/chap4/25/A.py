import sys


def solve():
    input_data = sys.stdin.read().split()
    H = int(input_data[0])
    W = int(input_data[1])
    c = []
    for i in range(H):
        c.append(input_data[2 + i])

    # dp[i][j]は(i,j)までの移動方法の数
    dp = [[-1 for _ in range(W + 1)] for _ in range(H + 1)]
    for i in range(1, H + 1):
        dp[i][0] = 0
    for j in range(W + 1):
        dp[0][j] = 0
    dp[1][1] = 1
    for i in range(1, H + 1):
        for j in range(1, W + 1):
            if i == 1 and j == 1:
                continue
            if c[i - 1][j - 1] == ".":
                dp[i][j] = dp[i][j - 1] + dp[i - 1][j]
            else:
                dp[i][j] = 0

    print(dp[H][W])


if __name__ == "__main__":
    solve()
