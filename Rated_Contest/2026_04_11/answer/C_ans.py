import sys


def solve():
    input_data = sys.stdin.read().split()
    N = int(input_data[0])
    L = [2 * int(x) for x in input_data[1 : N + 1]]

    def _sgn(x):
        if x > 0:
            return 1
        elif x < 0:
            return -1
        return 0

    best_ans = 0
    for i in range(1 << N):
        pos = 1
        cur = 0
        for j in range(N):
            pos_changed = pos
            if i & (1 << j):
                pos_changed += L[j]
            else:
                pos_changed -= L[j]
            if _sgn(pos_changed) * _sgn(pos) < 0:
                cur += 1
            pos = pos_changed
        best_ans = max(best_ans, cur)
    print(best_ans)


if __name__ == "__main__":
    solve()
