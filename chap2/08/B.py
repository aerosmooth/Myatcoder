N = int(input())
X = [None] * N
Y = [None] * N
point = [[0 for _ in range(1500 + 1)] for _ in range(1500 + 1)]
for i in range(N):
    X[i], Y[i] = map(int, input().split())
    point[X[i]][Y[i]] += 1
Q = int(input())
a = [None] * Q
b = [None] * Q
c = [None] * Q
d = [None] * Q
for i in range(Q):
    a[i], b[i], c[i], d[i] = map(int, input().split())

sum = [[0 for _ in range(1500 + 1)] for _ in range(1500 + 1)]

for i in range(1, 1500 + 1):
    for j in range(1, 1500 + 1):
        sum[i][j] = sum[i][j - 1] + point[i][j]

for j in range(1, 1500 + 1):
    for i in range(1, 1500 + 1):
        sum[i][j] += sum[i - 1][j]

for i in range(Q):
    print(
        sum[c[i]][d[i]]
        - sum[c[i]][b[i] - 1]
        - sum[a[i] - 1][d[i]]
        + sum[a[i] - 1][b[i] - 1]
    )
