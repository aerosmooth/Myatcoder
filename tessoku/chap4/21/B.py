import sys


def solve():
    input_data = sys.stdin.read().split()
    N = int(input_data[0])
    S = input_data[1]
    # dp[l][r]はS[l]からS[r]までの範囲において最大何文字を回文として追加できているか
    dp = [[0 for _ in range(N)] for _ in range(N)]
    for i in range(N):
        dp[i][i] = 1
    for i in range(N - 1):
        if S[i] == S[i + 1]:
            dp[i][i + 1] = 2
        else:
            dp[i][i + 1] = 1

    for LEN in range(2, N):
        for l in range(0, N - LEN):
            r = l + LEN
            dp[l][r] = max(dp[l][r - 1], dp[l + 1][r])
            if S[l] == S[r]:
                dp[l][r] = max(dp[l][r], dp[l + 1][r - 1] + 2)

    print(dp[0][N - 1])


if __name__ == "__main__":
    solve()
