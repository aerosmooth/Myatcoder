N, K = map(int, input().split())
A = list(map(int, input().split()))

right = min(A) * K
left = 0

while left < right:
    mid = (left + right) // 2
    num_print = 0
    for a in A:
        num_print += mid // a
    if num_print >= K:
        right = mid
    else:
        left = mid + 1
print(left)
