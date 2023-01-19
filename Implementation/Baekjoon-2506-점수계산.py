## 구현(Implementation)
## Baekjoon 2506 점수계산
## https://www.acmicpc.net/problem/2506

n = int(input())
check_list = list(map(int, input().split()))
answer = 0
stack = 0

for i in check_list:    
    if i == 1:
        stack += 1
        answer += stack
    else:
        stack = 0

print(answer)