import sys


def solve():
    input_data = sys.stdin.read().split()
    it = iter(input_data)
    N = int(next(it))
    K = int(next(it))
    L = [0] * N
    R = [0] * N
    intervals = []
    for i in range(N):
        L[i] = int(next(it))
        R[i] = int(next(it))
        intervals.append((R[i], L[i]))

    intervals.sort(key=lambda x: x[0])

    def check(x):
        count = 0
        last_r = -float("inf")

        for r, l in intervals:
            if l >= last_r + x:
                count += 1
                last_r = r
                if count >= K:
                    return True
        return False

    if not check(1):
        print("-1")
        return
    left = 1
    right = 10**9 + 1
    ans = -1

    while left <= right:
        mid = (left + right) // 2
        if check(mid):
            ans = mid
            left = mid + 1
        else:
            right = mid - 1

    print(ans)


if __name__ == "__main__":
    solve()
