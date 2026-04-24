N = int(input())
A = list(map(int, input().split()))
D = int(input())
L = [None] * D
R = [None] * D
for i in range(D):
    L[i], R[i] = map(int, input().split())

MAX_FROM_LEFT = [0] * (N + 2)
MAX_FROM_RIGHT = [0] * (N + 2)

for i in range(1, N + 1):
    MAX_FROM_LEFT[i] = max(MAX_FROM_LEFT[i - 1], A[i - 1])
    MAX_FROM_RIGHT[N + 1 - i] = max(MAX_FROM_RIGHT[N + 2 - i], A[N - i])

for i in range(D):
    print(max(MAX_FROM_LEFT[L[i] - 1], MAX_FROM_RIGHT[R[i] + 1]))
