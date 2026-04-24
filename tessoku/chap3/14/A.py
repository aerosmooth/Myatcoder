N, K = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))
D = list(map(int, input().split()))

A_and_B = []
for a in A:
    for b in B:
        A_and_B.append(a + b)

C_and_D = []
for c in C:
    for d in D:
        C_and_D.append(c + d)
C_and_D.sort()


def is_in(A: list, num: int):
    left = 0
    right = len(A)
    while left < right:
        mid = (left + right) // 2
        if A[mid] > num:
            right = mid
        elif A[mid] < num:
            left = mid + 1
        else:
            return True
    return False


for a in A_and_B:
    if is_in(C_and_D, K - a):
        print("Yes")
        exit(0)
print("No")
