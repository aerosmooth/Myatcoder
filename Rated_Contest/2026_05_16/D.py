import sys
import heapq


def solve():
    input_data = sys.stdin.read().split()
    X = int(input_data[0])
    Q = int(input_data[1])
    left = [-X]
    right = []
    index = 2
    for i in range(Q):
        a = int(input_data[index])
        index += 1
        b = int(input_data[index])
        index += 1

        for x in (a, b):
            if x <= -left[0]:
                heapq.heappush(left, -x)
            else:
                heapq.heappush(right, x)

        while len(left) > len(right) + 1:
            heapq.heappush(right, -heapq.heappop(left))

        while len(left) < len(right) + 1:
            heapq.heappush(left, -heapq.heappop(right))

        print(-left[0])


if __name__ == "__main__":
    solve()
