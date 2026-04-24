import sys


def solve():
    input_data = sys.stdin.read().split()
    N = int(input_data[0])
    h = [int(x) for x in input_data[1 : N + 1]]
    dp = [float("inf")] * N
    dp[0] = 0
    for i in range(N):
        if i + 1 < N:
            dp[i + 1] = min(dp[i + 1], dp[i] + abs(h[i + 1] - h[i]))
        if i + 2 < N:
            dp[i + 2] = min(dp[i + 2], dp[i] + abs(h[i + 2] - h[i]))
    print(dp[N - 1])


if __name__ == "__main__":
    solve()
