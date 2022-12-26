## 그리디 알고리즘
## 백준 1946 신입사원
## https://www.acmicpc.net/problem/1946

import sys
input = sys.stdin.readline

T = int(input())
zi_ong = list()

def solution(_zi_ong):
    answer = 1
    temp = _zi_ong[0][1]
    for i in range(0, len(_zi_ong)):
        if temp > _zi_ong[i][1]:
            temp = _zi_ong[i][1]
            answer += 1

    return answer

for i in range(T):
    N = int(input())

    for j in range(N):
        temp = list(map(int, input().split()))
        zi_ong.append(temp)
    
    zi_ong.sort()
    
    print(solution(zi_ong))
    
    zi_ong.clear()