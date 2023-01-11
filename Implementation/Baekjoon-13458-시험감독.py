## 구현(Implementation)
## Baekjoon 13458 시험 감독
## https://www.acmicpc.net/problem/13458

n = int(input())

people = list(map(int, input().split()))

B, C = map(int, input().split())

answer = n

for a in people:
    a -= B
    if a > 0:
        if a % C:
            answer += (a // C) + 1
        else:
            answer += (a // C)

print(answer)