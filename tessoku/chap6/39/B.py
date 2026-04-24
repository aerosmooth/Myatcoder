import sys
import heapq


def solve():
    input_data = sys.stdin.read().split()
    N = int(input_data[0])
    D = int(input_data[1])

    jobs = []
    for i in range(N):
        x = int(input_data[2 + 2 * i])
        y = int(input_data[3 + 2 * i])
        jobs.append((x, y))

    jobs.sort()

    heap = []
    ans = 0
    idx = 0

    for day in range(1, D + 1):
        while idx < N and jobs[idx][0] <= day:
            heapq.heappush(heap, -jobs[idx][1])
            idx += 1

        if heap:
            ans -= heapq.heappop(heap)

    print(ans)


if __name__ == "__main__":
    solve()
