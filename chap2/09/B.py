N = int(input())
A = [0] * N
B = [0] * N
C = [0] * N
D = [0] * N
for i in range(N):
    A[i], B[i], C[i], D[i] = map(int, input().split())
delta = [[0 for _ in range(1500 + 2)] for _ in range(1500 + 2)]
sum = [[0 for _ in range(1500 + 2)] for _ in range(1500 + 2)]
for i in range(N):
    delta[A[i]][B[i]] += 1
    delta[A[i]][D[i]] -= 1
    delta[C[i]][B[i]] -= 1
    delta[C[i]][D[i]] += 1

for j in range(1500 + 1):
    for i in range(1500 + 1):
        sum[i][j] = sum[i - 1][j] + delta[i][j]

for i in range(1500 + 1):
    for j in range(1500 + 1):
        sum[i][j] += sum[i][j - 1]

ans = 0
for j in range(1500 + 1):
    for i in range(1500 + 1):
        if sum[i][j] >= 1:
            ans += 1

print(ans)
