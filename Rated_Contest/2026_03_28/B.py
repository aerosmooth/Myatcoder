N, M = map(int, input().split())
A = [0] * N
B = [0] * N
for i in range(N):
    A[i], B[i] = map(int, input().split())

raiki = [0] * M
konki = [0] * M

for i in range(N):
    konki[A[i] - 1] += 1
    raiki[B[i] - 1] += 1

for i in range(M):
    print(raiki[i] - konki[i])
