import sys


def read_input():
    input_data = sys.stdin.read().split()
    H = int(input_data[0])
    W = int(input_data[1])
    S = [None] * H
    for i in range(H):
        S[i] = input_data[2 + i]
    return H, W, S


def solve():
    H, W, S = read_input()
    ans = 0
    for h1 in range(H):
        for h2 in range(h1, H):
            for w1 in range(W):
                for w2 in range(w1, W):
                    is_symmetric = True
                    for i in range(h1, h2 + 1):
                        for j in range(w1, w2 + 1):
                            sym_i = h1 + h2 - i
                            sym_j = w1 + w2 - j
                            if S[i][j] != S[sym_i][sym_j]:
                                is_symmetric = False
                                break
                        if not is_symmetric:
                            break
                    if is_symmetric:
                        ans += 1

    print(ans)


if __name__ == "__main__":
    solve()
