import sys
from collections import deque


def solve():
    input = sys.stdin.read().split()
    if not input:
        return

    H = int(input[0])
    W = int(input[1])
    S = input[2:]

    start = None
    goal = None

    for i in range(H):
        for j in range(W):
            if S[i][j] == "G":
                goal = (i, j)
            elif S[i][j] == "S":
                start = (i, j)
    # 上右下左
    dr = [-1, 0, 1, 0]
    dc = [0, 1, 0, -1]
    chars = ["U", "R", "D", "L"]
    # (前のr,前のc,前のd,行った操作文字)
    parents = [[[-2] * 4 for _ in range(W)] for _ in range(H)]

    queue = deque()
    sr, sc = start

    for nd in range(4):
        nr, nc = sr + dr[nd], sc + dc[nd]
        if 0 <= nr < H and 0 <= nc < W and S[nr][nc] != "#":
            queue.append((nr, nc, nd))
            parents[nr][nc][nd] = -1

    ans = None
    while queue:
        r, c, d = queue.popleft()
        if (r, c) == goal:
            ans = (r, c, d)
            break
        curr_cell = S[r][c]
        for nd in range(4):
            if curr_cell == "o" and nd != d:
                continue
            if curr_cell == "x" and nd == d:
                continue

            nr, nc = r + dr[nd], c + dc[nd]
            if not (0 <= nr < H and 0 <= nc < W):
                continue
            if S[nr][nc] == "#":
                continue
            if parents[nr][nc][nd] == -2:
                queue.append((nr, nc, nd))
                parents[nr][nc][nd] = d

    if ans is None:
        print("No")
    else:
        print("Yes")
        path = []
        r, c, d = ans
        while d != -1:
            prev_d = parents[r][c][d]
            path.append(chars[d])
            r -= dr[d]
            c -= dc[d]
            d = prev_d
        path.reverse()
        print("".join(path))


if __name__ == "__main__":
    solve()
