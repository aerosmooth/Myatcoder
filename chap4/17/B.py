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
    ans = [N]
    count = dp[N - 1]
    i = N - 1
    while i > 0:
        if i - 1 >= 0 and dp[i] == dp[i - 1] + abs(h[i] - h[i - 1]):
            ans.append(i)
            i -= 1
        elif i - 2 >= 0 and dp[i] == dp[i - 2] + abs(h[i] - h[i - 2]):
            ans.append(i - 1)
            i -= 2
    print(len(ans))
    ans.reverse()
    print(" ".join(map(str, ans)))


if __name__ == "__main__":
    solve()
