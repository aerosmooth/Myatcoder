S = input()
T = input()

N = len(S)
K = len(T)

dp = [-1] * (K + 1)
# dp[j]はTの先頭j文字を部分列として構成できるサタンのインデックス
total_count = 0
for R in range(N):
    dp[0] = R
    for j in range(K, 0, -1):  # 右から更新
        if S[R] == T[j - 1]:
            dp[j] = dp[j - 1]
    total_count += R - dp[K]
print(total_count)
