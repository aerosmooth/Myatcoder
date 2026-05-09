import heapq


def solve():
    Q = int(input())
    queries = [input().split() for _ in range(Q)]
    T = []
    for q in queries:
        if q[0] == "1":
            heapq.heappush(T, int(q[1]))
        elif q[0] == "2":
            print(T[0])
        elif q[0] == "3":
            heapq.heappop(T)


if __name__ == "__main__":
    solve()
