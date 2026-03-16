N = int(input())
A = list(map(int, input().split()))
Q = int(input())
X = []
for _ in range(Q):
    X.append(int(input()))

A.sort()


def count(A: list, q: int):
    left = 0
    right = N
    while left < right:
        mid = (left + right) // 2
        if A[mid] >= q:
            right = mid
        else:
            left = mid + 1

    return left


for q in X:
    print(count(A, q))
