N = int(input())
P = [0] * N
A = [0] * N
for i in range(N):
    P[i], A[i] = map(int, input().split())

dp = [[0 for _ in range(N + 1)] for _ in range(N + 1)]
# dp[i][j]は一番左がi番目、1番右がj番目のブロックの時の最大値を格納
# dp[i][i]の最大を求めたい
for LEN in reversed(range(0, N - 1)):
    for l in range(1, N - LEN + 1):
        r = l + LEN
        # 左側を消してきた場合
        score_l = 0
        if 0 <= l - 2 <= N - 1 and l <= P[l - 2] <= r:
            score_l = A[l - 2]
        # 右側を消してきた場合
        score_r = 0
        if 0 <= r <= N - 1 and l <= P[r] <= r:
            score_r = A[r]

        if 0 <= l - 1 and r + 1 <= N:
            dp[l][r] = max(dp[l - 1][r] + score_l, dp[l][r + 1] + score_r)
        elif l - 1 < 0 and r + 1 <= N:
            dp[l][r] = dp[l][r + 1] + score_r
        else:
            dp[l][r] = dp[l - 1][r] + score_l

ans = 0
for i in range(1, N + 1):
    ans = max(ans, dp[i][i])
print(ans)
