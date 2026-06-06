import sys


def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    N = int(input_data[0])
    K = int(input_data[1])
    M = int(input_data[2])

    v_per_c = {}

    for i in range(N):
        c = int(input_data[3 + 2 * i])
        v = int(input_data[4 + 2 * i])
        if c not in v_per_c:
            v_per_c[c] = []
        v_per_c[c].append(v)

    max_v_list = []
    remaining_values = []

    for c, v_list in v_per_c.items():
        v_list.sort(reverse=True)
        max_v_list.append(v_list[0])
        remaining_values.extend(v_list[1:])

    max_v_list.sort(reverse=True)

    answer = 0

    take_m = min(len(max_v_list), M)

    answer += sum(max_v_list[:take_m])

    remaining_values.extend(max_v_list[take_m:])

    remaining_values.sort(reverse=True)

    rem_count = K - take_m

    if rem_count > 0:
        answer += sum(remaining_values[:rem_count])

    print(answer)


if __name__ == "__main__":
    solve()
