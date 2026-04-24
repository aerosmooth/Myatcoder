import sys


def Enumerate(A: list):
    SUM_list = []
    A_len = len(A)
    for i in range(2**A_len):
        tmp = 0
        for j in range(A_len):
            if (i >> j) & 1:
                tmp += A[j]
        SUM_list.append((tmp, i))
    return SUM_list


def binary_search(A: list, num: int):
    left = 0
    right = len(A)
    while left < right:
        mid = (left + right) // 2
        if A[mid][0] < num:
            left = mid + 1
        elif A[mid][0] > num:
            right = mid
        else:
            return A[mid][1]
    return -1


def search(a: list, b: list, K):
    A = sorted(a)
    B = sorted(b)
    for i in range(len(A)):
        ind = binary_search(B, K - A[i][0])
        if ind != -1:
            return (A[i][1], ind)
    return (-1, -1)


def ten2two(num: int, length: int):
    ans = []
    for _ in range(length):
        ans.append(num % 2)
        num //= 2
    return ans


def solve():
    input_data = sys.stdin.read().split()
    N = int(input_data[0])
    S = int(input_data[1])
    A = [int(x) for x in input_data[2 : N + 2]]
    B = A[: N // 2]
    C = A[N // 2 :]
    D = Enumerate(B)
    E = Enumerate(C)

    ind_D, ind_E = search(D, E, S)
    if ind_E == -1 and ind_D == -1:
        print(-1)
        return
    binary_D = ten2two(ind_D, len(B))
    binary_E = ten2two(ind_E, len(C))
    ans = []
    for i in range(len(binary_D)):
        if binary_D[i] == 1:
            ans.append(i + 1)
    len_D = len(binary_D)
    for i in range(len(binary_E)):
        if binary_E[i] == 1:
            ans.append(len_D + i + 1)
    print(len(ans))
    for a in ans:
        print(a, end=" ")
    print()


if __name__ == "__main__":
    solve()
