N = int(input())
for i in range(1, N + 1):
    if i == N:
        print(f"{N - i + 1}")
    else:
        print(f"{N - i + 1}", end=",")
