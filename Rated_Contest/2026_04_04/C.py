N = int(input())
A = [0] * N
B = [0] * N
for i in range(N):
    A[i], B[i] = map(int, input().split())
M = int(input())
S = [""] * M
for i in range(M):
    S[i] = input()

chars = set()
for s in S:
    length = len(s)
    for p, char in enumerate(s):
        chars.add((length, p + 1, char))


for j in range(M):
    S_j = S[j]
    if len(S_j) != N:
        print("No")
        continue
    is_possible = True
    for i in range(N):
        sekitui = S_j[i]
        req_length = A[i]
        req_pos = B[i]

        if (req_length, req_pos, sekitui) not in chars:
            is_possible = False
            break
    if is_possible:
        print("Yes")
    else:
        print("No")
