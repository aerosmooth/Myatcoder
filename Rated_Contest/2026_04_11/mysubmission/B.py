import sys


def solve():
    input_data = sys.stdin.read().split()
    T = int(input_data[0])
    X = int(input_data[1])
    A = [0] * (T + 1)
    for i in range(T + 1):
        A[i] = int(input_data[2 + i])
    ans = {}
    ans[0] = A[0]
    bef_A = A[0]
    for i in range(1, T + 1):
        if abs(bef_A - A[i]) >= X:
            ans[i] = A[i]
            bef_A = A[i]
    for k, v in ans.items():
        print(f"{k} {v}")


if __name__ == "__main__":
    solve()
