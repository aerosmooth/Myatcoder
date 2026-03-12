N = int(input())
A = list(map(int, input().split()))
Q = int(input())
L = [0] * Q
R = [0] * Q
for i in range(Q):
    a, b = map(int, input().split())
    L[i], R[i] = a, b

sum = [0] * (N + 1)
for i in range(1, N + 1):
    sum[i] += sum[i - 1] + A[i - 1]

for i in range(Q):
    num_atari = sum[R[i]] - sum[L[i] - 1]
    num_sikou = R[i] - L[i] + 1
    if num_atari * 2 > num_sikou:
        print("win")
    elif num_atari * 2 < num_sikou:
        print("lose")
    else:
        print("draw")
