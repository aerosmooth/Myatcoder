import sys

sys.setrecursionlimit(10**6)


def solve():
    input_data = sys.stdin.read().split()
    T = int(input_data[0])
    index = 1
    for i in range(T):
        # 入力処理
        N = int(input_data[index])
        index += 1
        M = int(input_data[index])
        index += 1
        network = [[] for _ in range(N)]
        for _ in range(M):
            u = int(input_data[index]) - 1
            index += 1
            v = int(input_data[index]) - 1
            index += 1
            network[u].append(v)
            network[v].append(u)
        W = int(input_data[index])
        index += 1
        S = []
        for i in range(N):
            S.append(input_data[index])
            index += 1
        # dfs_flag[day][city] 0 = 未訪問, 1 = DFS中, 2 = 探索完了
        dfs_flag = [[0] * N for _ in range(W)]

        def dfs(day, city):
            if dfs_flag[day][city] == 1:
                return True
            if dfs_flag[day][city] == 2:
                return False

            dfs_flag[day][city] = 1
            next_day = (day + 1) % W

            if S[city][next_day] == "o":
                if dfs(next_day, city):
                    return True

            for next_city in network[city]:
                if S[next_city][next_day] == "o":
                    if dfs(next_day, next_city):
                        return True
            dfs_flag[day][city] = 2
            return False

        ok = False
        for city in range(N):
            if S[city][0] == "o":
                if dfs(0, city):
                    ok = True
                    break

        if ok:
            print("Yes")
        else:
            print("No")


if __name__ == "__main__":
    solve()
