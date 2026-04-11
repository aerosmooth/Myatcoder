import sys


def solve():
    input_data = sys.stdin.read().split()
    N = int(input_data[0])
    L = [int(x) for x in input_data[1 : N + 1]]
    ans = 0
    pos = 0.5
    for i in range(N):
        posi_mv = pos + L[i]
        neg_mv = pos - L[i]
        if abs(posi_mv) > abs(neg_mv):
            if neg_mv * pos < 0:
                ans += 1
            pos = neg_mv
        else:
            if posi_mv * pos < 0:
                ans += 1
            pos = posi_mv
    print(ans)


if __name__ == "__main__":
    solve()
