import sys


def solve():
    input_data = sys.stdin.read().split()
    N = int(input_data[0])
    A = []
    for i in range(N):
        A.append(int(input_data[1 + i]))
    LEN = 0  # LEN は L の長さ（例：L[3] まで書き込まれている場合 LEN=4）
    L = []  # 0 番目から始まることに注意
    dp = [None] * N  # 0 番目から始まることに注意

    def bisect(L: list, x: int):
        left = 0
        right = len(L)
        while left < right:
            mid = (left + right) // 2
            if L[mid] < x:
                left = mid + 1
            elif L[mid] > x:
                right = mid
            else:
                return mid
        return left

    for i in range(N):
        pos = bisect(L, A[i])
        dp[i] = pos
        if dp[i] >= LEN:
            L.append(A[i])
            LEN += 1
        else:
            L[dp[i]] = A[i]

    print(LEN)


if __name__ == "__main__":
    solve()
