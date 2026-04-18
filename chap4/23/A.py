import sys


def solve():
    input_data = sys.stdin.read().split()
    N = int(input_data[0])
    M = int(input_data[1])
    A = [[0] * N for _ in range(M)]
    for i in range(M):
        for j in range(N):
            A[i][j] = int(input_data[2 + i * N + j])

    # dp[i][j]は、クーポン券iまで使った時にjという集合で使うクーポンの数
    dp = [[10**9] * (2**N) for i in range(M + 1)]
    dp[0][0] = 0
    for i in range(1, M + 1):
        for j in range(2**N):
            # i番目のクーポンを使わなかった場合
            dp[i][j] = min(dp[i][j], dp[i - 1][j])
            # i番目のクーポンを使う場合
            # jとクーポン券iの和集合
            # 1ならすでに無料になっている
            already_free = [0] * N
            for k in range(N):
                if (j >> k) & 1:
                    already_free[k] = 1

            v = 0
            for k in range(N):
                if already_free[k] == 1 or A[i - 1][k] == 1:
                    v += 2**k
            dp[i][v] = min(dp[i][v], dp[i - 1][j] + 1)

    if dp[M][2**N - 1] == 10**9:
        print("-1")
    else:
        print(dp[M][2**N - 1])


if __name__ == "__main__":
    solve()
