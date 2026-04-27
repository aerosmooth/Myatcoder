import sys


def read_input():
    input_data = sys.stdin.read().split()
    N = int(input_data[0])
    K = int(input_data[1])
    A = [int(x) for x in input_data[2 : 2 + N]]

    return N, K, A


def solve():
    N, K, A = read_input()
    A.sort()
    num_dict = {}
    for i in range(N):
        if A[i] in num_dict:
            num_dict[A[i]] += A[i]
        else:
            num_dict[A[i]] = A[i]
    sorted_num_dict = list(sorted(num_dict.items(), key=lambda item: item[1]))
    current_type_count = len(sorted_num_dict)
    types_to_remove = current_type_count - K
    Answer = 0
    for i in range(types_to_remove):
        Answer += sorted_num_dict[i][1]
    print(Answer)


if __name__ == "__main__":
    solve()
