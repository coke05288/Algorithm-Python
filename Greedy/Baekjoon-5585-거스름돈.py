## 그리디 알고리즘
## 백준 5585 거스름돈
## https://www.acmicpc.net/problem/5585

coins = [500, 100, 50, 10, 5, 1]

answer = 0

n = 1000 - int(input())

for coin in coins:
    if n >= coin:
        answer += n // coin
        n %= coin

print(answer)