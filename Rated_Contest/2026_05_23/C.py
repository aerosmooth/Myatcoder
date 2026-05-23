import sys


def solve():
    input_data = sys.stdin.read().split()
    N = int(input_data[0])
    Q = int(input_data[1])
    index = 2
    C = [0] * (N + 1)

    cnt_ge = [0] * (Q + 1)
    cnt_ge[0] = N

    base = 0
    ans = []
    for _ in range(Q):
        q = int(input_data[index])
        index += 1
        x = int(input_data[index])
        index += 1
        if q == 1:
            v = C[x]
            C[x] = v + 1
            cnt_ge[v + 1] += 1

            if cnt_ge[base + 1] == N:
                base += 1
        else:
            if x + base <= Q:
                ans.append(cnt_ge[x + base])
            else:
                ans.append(0)

    for num in ans:
        print(num)


if __name__ == "__main__":
    solve()
