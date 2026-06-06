import sys


def solve():
    input_data = sys.stdin.read().split()
    N = int(input_data[0])
    M = int(input_data[1])
    a = [0 for _ in range(M + 1)]
    b = [0 for _ in range(M + 1)]
    for i in range(M):
        a[i + 1] = int(input_data[2 + 2 * i])
        b[i + 1] = int(input_data[3 + 2 * i])

    network = {}
    for i in range(M):
        A = a[i + 1]
        B = b[i + 1]

        min_node = min(A, B)
        max_node = max(A, B)
        if max_node not in network:
            network[max_node] = [min_node]
        else:
            network[max_node].append(min_node)

    answer = 0
    for node in network.values():
        if len(node) == 1:
            answer += 1
    print(answer)


if __name__ == "__main__":
    solve()
