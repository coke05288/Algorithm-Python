## Stack & Queue
## Baekjoon 1158 요세푸스 문제
## https://www.acmicpc.net/problem/1158

from collections import deque

queue = deque()
answer = []

n, k = map(int , input().split())

for i in range(1, n+1):
    queue.append(i)

while queue:
    for i in range(k-1):
        queue.append(queue.popleft())
    answer.append(queue.popleft())

print("<", end="")

for i in range(len(answer)-1):
    print(f"{answer[i]}, ", end="")
    
print(answer[-1], end="")    
print(">", end="")