Q = int(input())
heap = []


def push(val):
    heap.append(val)
    i = len(heap) - 1
    while i > 0:
        p = (i - 1) // 2
        if heap[p] > heap[i]:
            heap[p], heap[i] = heap[i], heap[p]
            i = p
        else:
            break


def pop():
    if len(heap) == 1:
        return heap.pop()

    val = heap[0]
    heap[0] = heap.pop()
    i = 0
    n = len(heap)

    while 1:
        left = 2 * i + 1
        right = 2 * i + 2
        small = i

        if left < n and heap[left] < heap[small]:
            small = left
        if right < n and heap[right] < heap[small]:
            small = right

        if small != i:
            heap[i], heap[small] = heap[small], heap[i]
            i = small
        else:
            break
    return val


for _ in range(Q):
    query, h = map(int, input().split())

    if query == 1:
        push(h)
    else:
        while heap and heap[0] <= h:
            pop()
    print(len(heap))
