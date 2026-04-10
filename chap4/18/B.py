import sys


def solve():
    input_data = sys.stdin.read().split()
    N = int(input_data[0])
    S = int(input_data[1])
    A = [int(x) for x in input_data[2 : N + 2]]
    # dp[i][j]はi枚のカードを使った時に合計をjにできるかどうか
    dp = [[None] * (S + 1) for i in range(N + 1)]
    dp[0][0] = True
    for i in range(1, S + 1):
        dp[0][i] = False
    for i in range(1, N + 1):
        for j in range(0, S + 1):
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
    if not dp[N][S]:
        print("-1")
        return
    Answer = []
    Place = S
    for i in reversed(range(1, N + 1)):
        if not dp[i - 1][Place]:
            if dp[i][Place - A[i - 1]]:
                Place -= A[i - 1]
                Answer.append(i)
    Answer.reverse()
    print(len(Answer))
    for a in Answer:
        print(a, end=" ")
    print()


if __name__ == "__main__":
    solve()
