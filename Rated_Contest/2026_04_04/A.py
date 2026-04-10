M, D = map(int, input().split())
go = [(1, 7), (3, 3), (5, 5), (7, 7), (9, 9)]
inp = (M, D)
if inp in go:
    print("Yes")
else:
    print("No")
