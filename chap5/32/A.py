import sys


def solve():
    input_data = sys.stdin.read().split()
    N = int(input_data[0])
    A = int(input_data[1])
    B = int(input_data[2])

    # dp[x]=True のとき勝ちの状態、dp[x]=False のとき負けの状態
    dp = [None] * (N + 1)
    for i in range(N + 1):
        if i >= A and not dp[i - A]:
            dp[i] = True
        elif i >= B and not dp[i - B]:
            dp[i] = True
        else:
            dp[i] = False

    # print(dp)
    if dp[N]:
        print("First")
    else:
        print("Second")


if __name__ == "__main__":
    solve()
