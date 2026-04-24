D = int(input())
N = int(input())
L = []
R = []
for _ in range(N):
    l, r = map(int, input().split())
    L.append(l)
    R.append(r)

result = [0] * (D + 2)
for n in range(N):
    result[L[n]] += 1
    result[R[n] + 1] -= 1

tmp_result = 0
for d in range(1, 1 + D):
    tmp_result += result[d]
    print(tmp_result)
