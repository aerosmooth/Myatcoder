N, Q = map(int, input().split())
A = list(map(int, input().split()))
L = []
R = []
for i in range(Q):
    tmp_l, tmp_r = map(int, input().split())
    L.append(tmp_l)
    R.append(tmp_r)

sum = [0 for _ in range(N + 1)]
for i in range(1, 1 + N):
    sum[i] = sum[i - 1] + A[i - 1]
for i in range(Q):
    print(sum[R[i]] - sum[L[i] - 1])
