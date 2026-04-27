import sys


def read_input():
    input_data = sys.stdin.read().split()
    N = int(input_data[0])
    Q = int(input_data[1])
    C = []
    P = []
    for i in range(Q):
        C.append(int(input_data[2 + 2 * i]))
        P.append(int(input_data[3 + 2 * i]))

    return N, Q, C, P


def solve():
    N, Q, C, P = read_input()
    # カードの山の初期化
    card_moutain = []
    card2mountain = [0]
    card_moutain.append([])
    for i in range(N):
        card_moutain.append([i + 1])
        card2mountain.append(i + 1)

    for i in range(Q):
        c, p = C[i], P[i]
        c_mountain = card2mountain[c]
        p_mountain = card2mountain[p]

        target_mountain_list = card_moutain[c_mountain]
        c_index = target_mountain_list.index(c)
        moving_cards = target_mountain_list[c_index:]

        del target_mountain_list[c_index:]

        for card in moving_cards:
            card_moutain[p_mountain].append(card)
            card2mountain[card] = p_mountain
    for i in range(1, N + 1):
        print(len(card_moutain[i]), end=" ")

    print()


if __name__ == "__main__":
    solve()
