
T = int(input())

dp = [[0 for _ in range(31) ] for _ in range(31)]

for i in range(1, 31):
    dp[i][1] = 1
    dp[i][i] = 1


for i in range(2, 31):
    for j in range(2, 31):
        if i > j :
            dp[i][j] = dp[i-1][j] + dp[i-1][j-1]

for _ in range(T):
    N, M = map(int, input().split())
    print(dp[M+1][N+1])