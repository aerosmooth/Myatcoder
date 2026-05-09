import sys


def solve():
    input_data = sys.stdin.read().split()
    N = int(input_data[0])
    K = int(input_data[1])
    A = [int(x) for x in input_data[2 : 2 + N]]
    left = 0
    right = 5 * 10**18

    def is_over(X):
        times = 0
        for i in range(N):
            if A[i] < X:
                diff = X - A[i]
                times += (diff + i) // (i + 1)
                if times > K:
                    return False
        return True

    while right > left + 1:
        mid = (left + right) // 2
        if is_over(mid):
            left = mid
        else:
            right = mid

    print(left)


if __name__ == "__main__":
    solve()
