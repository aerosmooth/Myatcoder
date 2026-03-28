N, K = map(int, input().split())
A = list(map(int, input().split()))
for i in range(N):
    A[i] %= K
A.sort()

ans = A[-1] - A[0]
for i in range(N - 1):
    tmp_ans = A[i] + K - A[i + 1]
    if tmp_ans < ans:
        ans = tmp_ans
print(ans)
