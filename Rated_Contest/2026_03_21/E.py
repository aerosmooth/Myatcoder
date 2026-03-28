import sys


def solve():
    # 入力を一括で読み込む（高速化）
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    X = input_data[0]
    Y = input_data[1]
    Q = int(input_data[2])

    # === 1. XとYの累積和を事前計算 ===
    # pref_x[i][c] は、Xの先頭i文字に含まれるアルファベットcの個数
    len_x = len(X)
    pref_x = [[0] * 26 for _ in range(len_x + 1)]
    for i in range(len_x):
        for c in range(26):
            pref_x[i + 1][c] = pref_x[i][c]
        pref_x[i + 1][ord(X[i]) - 97] += 1

    len_y = len(Y)
    pref_y = [[0] * 26 for _ in range(len_y + 1)]
    for i in range(len_y):
        for c in range(26):
            pref_y[i + 1][c] = pref_y[i][c]
        pref_y[i + 1][ord(Y[i]) - 97] += 1

    # === 2. S_k の長さと、各文字の総数を事前計算 ===
    # k=1 が X、k=2 が Y
    length_arr = [0, len_x, len_y]
    tot = [[0] * 26 for _ in range(3)]
    for c in range(26):
        tot[1][c] = pref_x[len_x][c]
        tot[2][c] = pref_y[len_y][c]

    k = 3
    # 10^18 を超えるまで（k=90付近）テーブルを作成
    while length_arr[-1] < 10**18:
        length_arr.append(length_arr[k - 1] + length_arr[k - 2])
        new_tot = [0] * 26
        for c in range(26):
            new_tot[c] = tot[k - 1][c] + tot[k - 2][c]
        tot.append(new_tot)
        k += 1

    # === 3. 先頭 n 文字に含まれる対象文字 target_c の個数を求める関数 ===
    def calc(n, target_c):
        if n == 0:
            return 0

        ans = 0
        # 探索開始地点は、長さが n 以上となる十分大きな k
        curr_k = len(length_arr) - 1

        while curr_k > 2:
            prev_len = length_arr[curr_k - 1]
            if n <= prev_len:
                # 前半部分に完全に収まる場合
                curr_k -= 1
            else:
                # 前半部分を丸ごと含み、後半部分にはみ出す場合
                ans += tot[curr_k - 1][target_c]
                n -= prev_len
                curr_k -= 2

        # 最終的に X(k=1) か Y(k=2) に到達したら、累積和から拾う
        if curr_k == 1:
            ans += pref_x[n][target_c]
        elif curr_k == 2:
            ans += pref_y[n][target_c]

        return ans

    # === クエリ処理 ===
    idx = 3
    out = []
    for _ in range(Q):
        L = int(input_data[idx])
        R = int(input_data[idx + 1])
        # 文字を 0-25 の数値に変換
        C = ord(input_data[idx + 2]) - 97
        idx += 3

        # R文字目までの個数 - (L-1)文字目までの個数
        ans = calc(R, C) - calc(L - 1, C)
        out.append(str(ans))

    print("\n".join(out))


if __name__ == "__main__":
    solve()
