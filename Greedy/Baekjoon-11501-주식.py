## 그리디 알고리즘
## 백준 11501 주식
## https://www.acmicpc.net/problem/11501

T = int(input())

def solution(day_prices):
    answer = 0
    max_price = max(day_prices)

    for i in range(len(day_prices)):
        if max_price == day_prices[i] and i != len(day_prices)-1:
            max_price = max(day_prices[i+1:])
            continue
        else:
            answer += max_price - day_prices[i]

    return answer
    

for _ in range(T):
    N = int(input())
    day_prices = list(map(int, input().split()))
    
    print(solution(day_prices))

