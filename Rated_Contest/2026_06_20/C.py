import sys
from bisect import bisect_right


def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    it = iter(input_data)
    N = int(next(it))
    H, L = [0] * N, [0] * N
    for i in range(N):
        H[i] = int(next(it))
        L[i] = int(next(it))
    Q = int(next(it))
    T = [int(next(it)) for _ in range(Q)]
    aft_max = [0] * N
    current_max = 0
    for i in range(N - 1, -1, -1):
        if H[i] > current_max:
            current_max = H[i]
        aft_max[i] = current_max
    ans = []
    for t in T:
        idx = bisect_right(L, t)
        ans.append(str(aft_max[idx]))
    print("\n".join(ans))


if __name__ == "__main__":
    main()
