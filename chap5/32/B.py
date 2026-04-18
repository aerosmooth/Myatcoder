import sys


def solve():
    input_data = sys.stdin.read().split()
    N = int(input_data[0])
    K = int(input_data[1])
    a = []
    for i in range(K):
        a.append(int(input_data[2 + i]))

    # dp[i]がTrueの時、i個残っている状況で先手が勝つ
    dp = [None] * (N + 1)
    dp[0] = False
    a.sort()
    for i in range(1, N + 1):
        for j in range(K):
            # a[j]個消費して相手が負ける状況なら、こちらは勝てる
            if i >= a[j] and not dp[i - a[j]]:
                dp[i] = True

    if dp[N]:
        print("First")
    else:
        print("Second")


if __name__ == "__main__":
    solve()
