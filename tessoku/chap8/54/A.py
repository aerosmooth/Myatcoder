def solve():
    Q = int(input())
    queries = [input().split() for _ in range(Q)]

    Map = {}
    for q in queries:
        if q[0] == "1":
            Map[q[1]] = int(q[2])
        elif q[0] == "2":
            print(Map[q[1]])


if __name__ == "__main__":
    solve()
