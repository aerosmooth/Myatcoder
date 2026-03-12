H, W = map(int, input().split())
X = []
for _ in range(H):
    tmp = list(map(int, input().split()))
    X.append(tmp)
Q = int(input())
A = []
B = []
C = []
D = []
for _ in range(Q):
    a, b, c, d = map(int, input().split())
    A.append(a)
    B.append(b)
    C.append(c)
    D.append(d)

sum = [[0 for _ in range(W + 1)] for _ in range(H + 1)]
for i in range(1, H + 1):
    for j in range(1, W + 1):
        sum[i][j] = sum[i][j - 1] + X[i - 1][j - 1]

for j in range(1, W + 1):
    for i in range(1, H + 1):
        sum[i][j] += sum[i - 1][j]

for i in range(Q):
    print(
        sum[C[i]][D[i]]
        - sum[C[i]][B[i] - 1]
        - sum[A[i] - 1][D[i]]
        + sum[A[i] - 1][B[i] - 1]
    )
