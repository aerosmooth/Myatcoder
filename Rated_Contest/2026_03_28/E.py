import sys

input_data = sys.stdin.read().split()
if not input_data:
    exit()
N = int(input_data[0])
idx = 1
A = [[0] * N for _ in range(N)]
for i in range(N):
    for j in range(N):
        if i == j:
            A[i][j] = 0
        elif j > i:
            A[i][j] = int(input_data[idx])
            A[j][i] = A[i][j]
            idx += 1
INF = 10**18
used = [False] * N
dist = [INF] * N
parent = [-1] * N

dist[0] = 0

for _ in range(N):
    v = -1
    for u in range(N):
        if not used[u] and (v == -1 or dist[u] < dist[v]):
            v = u

    used[v] = True

    for u in range(N):
        if not used[u] and A[v][u] < dist[u]:
            dist[u] = A[v][u]
            parent[u] = v

tree = [[] for _ in range(N)]
for i in range(1, N):
    p = parent[i]
    tree[i].append((p, A[i][p]))
    tree[p].append((i, A[i][p]))


def dfs(start):
    stack = [(start, 0, -1)]

    while stack:
        v, d, par = stack.pop()

        if A[start][v] != d:
            return False

        for next_node, w in tree[v]:
            if next_node != par:
                stack.append((next_node, d + w, v))

    return True


for i in range(N):
    if not dfs(i):
        print("No")
        exit()

print("Yes")
