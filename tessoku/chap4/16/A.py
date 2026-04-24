N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

min_min = [None] * N
min_min[0] = 0
for i in range(1, N):
    if i >= 2:
        min_min[i] = min(min_min[i - 1] + A[i - 1], min_min[i - 2] + B[i - 2])
    else:
        min_min[i] = min_min[i - 1] + A[i - 1]
print(min_min[N - 1])
