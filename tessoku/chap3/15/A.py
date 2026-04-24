N = int(input())
A = list(map(int, input().split()))

C = A.copy()
A.sort()
B = [0] * N
count = 1
for i in range(len(A)):
    if i == 0:
        B[i] = 1
        count += 1
    else:
        if A[i] == A[i - 1]:
            B[i] = B[i - 1]
        else:
            B[i] = count
            count += 1
AB = {}
for i in range(len(A)):
    AB[A[i]] = B[i]

for c in C:
    print(AB[c], end=" ")
