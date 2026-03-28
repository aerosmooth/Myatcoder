H, W = map(int, input().split())
S = [[None for _ in range(W)] for _ in range(H)]
for i in range(H):
    S[i] = input()

# 外に漏れ出るならTrue
Result = [[False for _ in range(W)] for _ in range(H)]

while True:
    changed = False

    for i in range(H):
        for j in range(W):
            if S[i][j] == ".":
                if i == 0 or j == 0 or i == H - 1 or j == W - 1:
                    if not Result[i][j]:
                        Result[i][j] = True
                        changed = True
                elif not Result[i][j] and (Result[i][j - 1] or Result[i - 1][j]):
                    Result[i][j] = True
                    changed = True

    for i in reversed(range(H)):
        for j in reversed(range(W)):
            if S[i][j] == ".":
                if i == 0 or j == 0 or i == H - 1 or j == W - 1:
                    if not Result[i][j]:
                        Result[i][j] = True
                        changed = True
                elif not Result[i][j] and (Result[i][j + 1] or Result[i + 1][j]):
                    Result[i][j] = True
                    changed = True

    if not changed:
        break

result = [[False for _ in range(W)] for _ in range(H)]
for i in range(H):
    for j in range(W):
        if S[i][j] == "." and not Result[i][j]:
            result[i][j] = True


Answer = [[0 for _ in range(W)] for _ in range(H)]
count = 0


def fill_True(result, i, j, num):
    if result[i][j + 1] and Answer[i][j + 1] == 0:
        Answer[i][j + 1] = num
        fill_True(result, i, j + 1, num)

    if result[i + 1][j] and Answer[i + 1][j] == 0:
        Answer[i + 1][j] = num
        fill_True(result, i + 1, j, num)

    if result[i - 1][j] and Answer[i - 1][j] == 0:
        Answer[i - 1][j] = num
        fill_True(result, i - 1, j, num)

    if result[i][j - 1] and Answer[i][j - 1] == 0:
        Answer[i][j - 1] = num
        fill_True(result, i, j - 1, num)


for i in range(1, H - 1):
    for j in range(1, W - 1):
        if result[i][j] and Answer[i][j] == 0:
            count += 1
            Answer[i][j] = count
            fill_True(result, i, j, count)
# for i in Answer:
#     print(i)
print(count)
