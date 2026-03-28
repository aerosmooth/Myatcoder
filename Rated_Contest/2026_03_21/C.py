import re


H, W = map(int, input().split())
S = [[None for _ in range(W)] for _ in range(H)]
for i in range(H):
    S[i] = input()

# 外に漏れ出るならTrue
Result = [[False for _ in range(W)] for _ in range(H)]

stack = []
for i in range(H):
    for j in range(W):
        if S[i][j] == "." and (i == 0 or j == 0 or i == H - 1 or j == W - 1):
            stack.append((i, j))
while stack:
    r, c = stack.pop()
    for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        nr, nc = r + dr, c + dc
        if 0 <= nr < H and 0 <= nc < W:
            if S[nr][nc] == "." and not Result[nr][nc]:
                Result[nr][nc] = True
                stack.append((nr, nc))
result = [[False for _ in range(W)] for _ in range(H)]
for i in range(H):
    for j in range(W):
        if S[i][j] == "." and not Result[i][j]:
            result[i][j] = True


Answer = [[0 for _ in range(W)] for _ in range(H)]
count = 0

for i in range(1, H - 1):
    for j in range(1, W - 1):
        if result[i][j] and Answer[i][j] == 0:
            count += 1
            Answer[i][j] = count

            stack = [(i, j)]
            while stack:
                r, c = stack.pop()
                for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    nr, nc = r + dr, c + dc
                    if result[nr][nc] and Answer[nr][nc] == 0:
                        Answer[nr][nc] = count
                        stack.append((nr, nc))


# for i in Answer:
#     print(i)
print(count)
