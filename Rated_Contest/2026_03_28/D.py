N = int(input())

pow_len = [[] for _ in range(30)]
for i in range(30):
    p = str(1 << i)
    if len(p) <= 9:
        pow_len[len(p)].append(p)

dp = [set() for _ in range(10)]
dp[0].add("")

for len in range(1, 10):
    for p_len in range(1, len + 1):
        for p in pow_len[p_len]:
            for prefix in dp[len - p_len]:
                dp[len].add(prefix + p)

ans = set()
for l in range(1, 10):
    for s in dp[l]:
        ans.add(int(s))

sans = sorted(list(ans))
print(sans[N - 1])
