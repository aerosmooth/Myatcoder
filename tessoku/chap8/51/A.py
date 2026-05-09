import sys
from collections import deque


def get_index_input(input_data: list[str], index: list[int]) -> str:
    query = input_data[index[0]]
    index[0] += 1
    return query


def solve():
    input_data = sys.stdin.read().split()
    index = [0]
    Q = int(get_index_input(input_data, index))
    book = deque()
    for _ in range(Q):
        query = int(get_index_input(input_data, index))
        if query == 1:
            book.append(get_index_input(input_data, index))
        elif query == 2:
            print(book[-1])
        elif query == 3:
            book.pop()
        else:
            raise ValueError(f"{query} is not supported.")


if __name__ == "__main__":
    solve()
