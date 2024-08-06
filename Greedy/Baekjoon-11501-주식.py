## 그리디 알고리즘
## 백준 11501 주식
## https://www.acmicpc.net/problem/11501

import sys
input = sys.stdin.readline

T = int(input())

def solution(day_prices):
    answer = 0
    max_price = 0

    for i in range(len(day_prices) - 1, -1, -1):
        if max_price < day_prices[i]:
            max_price = day_prices[i]
        else:
            answer += max_price - day_prices[i]
    return answer
    

for _ in range(T):
    N = int(input())
    day_prices = list(map(int, input().split()))

    if day_prices[0] * 3 == sum(day_prices):
        print(0)
    else:
        print(solution(day_prices))

