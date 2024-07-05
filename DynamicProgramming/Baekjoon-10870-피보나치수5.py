
N = int(input())

dp = [0] * (N + 2)

dp[0] = 0
dp[1] = 1

if N < 2:
    print(dp[N])
else:
    for i in range(2, N + 1):
        dp[i] = dp[i - 2] + dp[i - 1]
    print(dp[N])
