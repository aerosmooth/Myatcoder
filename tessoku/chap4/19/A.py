N, W = map(int, input().split())
w = [0] * N
v = [0] * N
for i in range(N):
    w[i], v[i] = map(int, input().split())

# dp[i][j]はi個までの品を使って、重さj以下の制限における最大の価値を格納
dp = [[None for _ in range(W + 1)] for _ in range(N + 1)]
for i in range(N + 1):
    dp[i][0] = 0
for j in range(W + 1):
    dp[0][j] = 0

for i in range(1, N + 1):
    for j in range(1, W + 1):
        tmp = dp[i - 1][j]
        if j >= w[i - 1]:
            tmp = max(dp[i - 1][j - w[i - 1]] + v[i - 1], tmp)
        dp[i][j] = tmp
print(dp[N][W])
