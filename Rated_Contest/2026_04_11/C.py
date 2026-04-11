import sys


def solve():
    input_data = sys.stdin.read().split()
    N = int(input_data[0])
    L = [int(x) for x in input_data[1 : N + 1]]
    ans = 0
    pos = 0.5

    def dfs(i, pos, cross):
        if i == N:
            return cross
        pos_mv = pos + L[i]
        plus_cross = 1 if pos * pos_mv < 0 else 0
        res_plus = dfs(i + 1, pos_mv, cross + plus_cross)

        neg_mv = pos - L[i]
        plus_cross = 1 if pos * neg_mv < 0 else 0
        res_minus = dfs(i + 1, neg_mv, cross + plus_cross)

        return res_plus if res_plus > res_minus else res_minus

    ans = dfs(0, 0.5, 0)
    print(ans)


if __name__ == "__main__":
    solve()
