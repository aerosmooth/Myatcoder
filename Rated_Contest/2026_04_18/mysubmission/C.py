import sys


def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    N = int(input_data[0])
    M = int(input_data[1])
    A = []
    B = []
    for i in range(M):
        A.append(int(input_data[2 + 2 * i]))
        B.append(int(input_data[3 + 2 * i]))

    can_get = [[] for _ in range(N + 1)]

    for i in range(M):
        can_get[A[i]].append(B[i])

    ans_set = set()
    ans_set.add(1)
    stack = [1]

    while stack:
        current_stack = stack.pop()
        for next in can_get[current_stack]:
            if next not in ans_set:
                stack.append(next)
                ans_set.add(next)

    print(len(ans_set))


if __name__ == "__main__":
    solve()
