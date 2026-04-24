import sys


def solve():
    input_data = sys.stdin.read().split()
    S = input_data[0]
    T = input_data[1]
    len_S = len(S)
    len_T = len(T)
    # dp[i][j]はS[i - 1],T[j - 1]まででの最小数
    INF = 1e10
    dp = [[INF for _ in range(len_T + 1)] for _ in range(len_S + 1)]
    for i in range(len_S + 1):
        dp[i][0] = i
    for j in range(len_T + 1):
        dp[0][j] = j

    for i in range(1, len_S + 1):
        for j in range(1, len_T + 1):
            tmp = min(dp[i][j - 1] + 1, dp[i - 1][j] + 1)
            if S[i - 1] == T[j - 1]:
                tmp = min(dp[i - 1][j - 1], tmp)
            else:
                tmp = min(tmp, dp[i - 1][j - 1] + 1)
            dp[i][j] = tmp
    print(dp[len_S][len_T])


if __name__ == "__main__":
    solve()
