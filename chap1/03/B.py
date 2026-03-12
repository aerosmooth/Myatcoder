N = int(input())
A = list(map(int, input().split()))
ANSWER = False

for i in range(N):
    for j in range(N):
        if i != j:
            for k in range(N):
                if i != k and j != k:
                    if (A[i] + A[j] + A[k]) == 1000:
                        ANSWER = True

if ANSWER:
    print("Yes")
else:
    print("No")
