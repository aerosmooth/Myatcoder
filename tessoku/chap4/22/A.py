import sys


def solve():
    input_data = sys.stdin.read().split()
    N = int(input_data[0])
    A = [int(x) for x in input_data[1:N]]
    B = [int(x) for x in input_data[N : 2 * N - 1]]
    dp = [-(10**9)] * (N + 1)
    dp[1] = 0
    for i in range(1, N):
        dp[A[i - 1]] = max(dp[A[i - 1]], dp[i] + 100)
        dp[B[i - 1]] = max(dp[B[i - 1]], dp[i] + 150)

    print(dp[N])


if __name__ == "__main__":
    solve()
