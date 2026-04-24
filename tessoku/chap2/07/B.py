T = int(input())
N = int(input())
L = []
R = []
for _ in range(N):
    l, r = map(int, input().split())
    L.append(l)
    R.append(r)

result = [0] * (T + 1)

for i in range(N):
    result[L[i]] += 1
    result[R[i]] -= 1

tmp = 0
for i in range(T):
    tmp += result[i]
    print(tmp)
