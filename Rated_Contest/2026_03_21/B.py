N = int(input())
C = []
for i in range(N - 1):
    t = list(map(int, input().split()))
    C.append(t)

Answer = False
for a in range(N - 2):
    for b in range(a + 1, N - 1):
        for c in range(b + 1, N):
            if C[a][c - a - 1] > C[a][b - a - 1] + C[b][c - b - 1]:
                Answer = True
if Answer:
    print("Yes")
else:
    print("No")
