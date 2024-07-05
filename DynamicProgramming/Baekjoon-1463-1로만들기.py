## Dynamic Programming
## Baekjoon 1463 계단오르기
## https://www.acmicpc.net/problem/1463

X = int(input())

DP = [0] * (X + 1)

for i in range(2, X + 1):
    # 3번 연산 1 빼기
    DP[i] = DP[i-1] + 1

    # 2번 연산 3 나누기
    if i % 3 == 0:
        DP[i] = min(DP[i] , DP[i//3] + 1)
    if i % 2 == 0:
        DP[i] = min(DP[i] , DP[i//2] + 1)
    
print(DP[X])