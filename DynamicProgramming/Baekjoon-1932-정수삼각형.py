## Dynamic Programming
## Baekjoon 1932 정수삼각형
## https://www.acmicpc.net/problem/11932

N = int(input())
dp = []

for i in range(N):
    dp.append(list(map(int, input().split())) + [0] * (N - (i + 1)))

for i in range(1, N):
    for j in range(N):
        if j == 0:
            dp[i][j] = dp[i][j] + dp[i-1][j]    
        elif j == N-1:
            dp[i][j] = dp[i][j] + dp[i-1][j-1]
        else:    
            dp[i][j] = max(dp[i][j] + dp[i-1][j-1], dp[i][j] + dp[i-1][j])

print(max(dp[N-1]))