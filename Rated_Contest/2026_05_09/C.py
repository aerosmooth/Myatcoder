import sys


def solve():
    input_data = sys.stdin.read().split()
    N = int(input_data[0])
    K = int(input_data[1])
    L = []
    A = []
    A_len = []
    start = 2
    for i in range(N):
        L.append(int(input_data[start]))
        start += 1
        x = [int(x) for x in input_data[start : start + L[i]]]
        start += L[i]
        A.append(x)
        A_len.append(len(x))

    C = [int(x) for x in input_data[start : start + N]]
    K -= 1
    B_len = 0
    for i in range(N):
        tmp = A_len[i] * C[i]
        if B_len + tmp > K:
            print(A[i][(K - B_len) % A_len[i]])
            return
        B_len += tmp


if __name__ == "__main__":
    solve()
