N, S = map(int, input().split())
A = list(map(int, input().split()))

# dp[i][j]は、i枚のカードを使って、合計jにできるかどうか
dp = [[None for _ in range(S + 1)] for _ in range(N + 1)]
for i in range(N + 1):
    dp[i][0] = True
for j in range(S + 1):
    dp[0][j] = False
dp[0][0] = True

for i in range(1, N + 1):
    for j in range(1, S + 1):
        if j < A[i - 1]:
            if dp[i - 1][j]:
                dp[i][j] = True
            else:
                dp[i][j] = False
        else:
            if dp[i - 1][j] or dp[i - 1][j - A[i - 1]]:
                dp[i][j] = True
            else:
                dp[i][j] = False

if dp[N][S]:
    print("Yes")
else:
    print("No")
