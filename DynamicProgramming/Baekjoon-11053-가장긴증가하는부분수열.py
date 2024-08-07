## Dynamic Programming
## Baekjoon 11053 가장 긴 증가하는 부분 수열
## https://www.acmicpc.net/problem/11053

N = int(input())
A = list(map(int, input().split()))

def solution():
    dp = [1] * N
    for i in range(1, N):
        for j in range(i):
            if A[i] > A[j]:
                dp[i] = max(dp[i], dp[j] + 1)
    return max(dp)
            
print(solution())