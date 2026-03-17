N, K = map(int, input().split())
A = list(map(int, input().split()))

count = 0
for i in range(N):
    left = i + 1
    right = N
    while left < right:
        mid = (left + right) // 2
        if A[mid] - A[i] <= K:
            left = mid + 1
        else:
            right = mid
    count += left - i - 1
print(count)
