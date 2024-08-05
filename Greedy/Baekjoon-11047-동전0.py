## 그리디 알고리즘
## 백준 11047 동전0
## https://www.acmicpc.net/problem/11047

N, K = map(int, input().split())
coins = list()

for _ in range(N):
    coins.append(int(input()))

def solution(N, K, coins):
    answer = 0

    while K > 0:
        temp_coin = 0
        for coin in reversed(coins):
            if coin <= K:
                temp_coin = coin
                break
        
        K -= temp_coin
        answer += 1
    
    return answer

print(solution(N, K, coins))