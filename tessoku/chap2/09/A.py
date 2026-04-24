H, W, N = map(int, input().split())
A = []
B = []
C = []
D = []
for _ in range(N):
    a, b, c, d = map(int, input().split())
    A.append(a)
    B.append(b)
    C.append(c)
    D.append(d)

sum = [[0 for _ in range(W + 2)] for _ in range(H + 2)]
delta = [[0 for _ in range(W + 2)] for _ in range(H + 2)]

for i in range(N):
    delta[A[i]][B[i]] += 1
    delta[A[i]][D[i] + 1] += -1
    delta[C[i] + 1][B[i]] += -1
    delta[C[i] + 1][D[i] + 1] += 1

for i in range(1, 1 + H):
    for j in range(1, 1 + W):
        sum[i][j] = sum[i][j - 1] + delta[i][j]

for j in range(1, 1 + W):
    for i in range(1, 1 + H):
        sum[i][j] += sum[i - 1][j]

for i in range(1, H + 1):
    for j in range(1, W + 1):
        print(sum[i][j], end=" ")
    print("")
