import sys
from collections import deque


def solve():
    input = sys.stdin.read().split()
    H = int(input[0])
    W = int(input[1])
    S = input[2:]

    start = None
    goal = None
    for i in range(H):
        for j in range(W):
            if S[i][j] == "S":
                start = (i, j)
            if S[i][j] == "G":
                goal = (i, j)
    dr = [-1, 0, 1, 0]
    dc = [0, 1, 0, -1]
    chars = ["U", "R", "D", "L"]

    # parents[nr][nc][nd]は(今いるi、今いるj、直前の移動方法)で-2なら未侵入、-1なら初期値への最後の道を表す
    parents = [[[-2] * 4 for _ in range(W)] for _ in range(H)]
    queue = deque()
    sr, sc = start
    for nd in range(4):
        nr, nc = sr + dr[nd], sc + dc[nd]
        if 0 <= nr < H and 0 <= nc < W and S[nr][nc] != "#":
            parents[nr][nc][nd] = -1
            queue.append((nr, nc, nd))

    ans = None
    while queue:
        r, c, d = queue.popleft()
        if (r, c) == goal:
            ans = (r, c, d)
            break
        curr_cell = S[r][c]
        for nd in range(4):
            nr, nc = r + dr[nd], c + dc[nd]
            if not (0 <= nr < H and 0 <= nc < W):
                continue
            if curr_cell == "o" and d != nd:
                continue
            if curr_cell == "x" and d == nd:
                continue
            if parents[nr][nc][nd] == -2:
                parents[nr][nc][nd] = d
                queue.append((nr, nc, nd))

    if ans is None:
        print("No")
        return
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
