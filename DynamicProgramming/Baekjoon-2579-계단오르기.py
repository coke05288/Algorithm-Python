## Dynamic Programming
## Baekjoon 2579 계단오르기
## https://www.acmicpc.net/problem/2579

N = int(input())

DP = [0] * 301
stairs = [0] * 301

for i in range(N):
    stairs[i] = int(input())

DP[0] = stairs[0]
DP[1] = max(stairs[0] + stairs[1], stairs[1])
DP[2] = max(stairs[0] + stairs[2], stairs[1] + stairs[2])

for i in range(3, N):
    DP[i] = max(DP[i-2] + stairs[i], DP[i-3] + stairs[i] + stairs[i-1])
    
print(DP[N-1])