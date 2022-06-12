## DFS & BFS
## Baekjoon 1260 DFS와 BFS
## https://www.acmicpc.net/problem/1260
from collections import deque

# N, M, V 입력
N, M, V = map(int, input().split(" "))

# 그래프 입력(인접리스트) 및 value 값 정렬
graph = [list() for _ in range(N+1)]

for _ in range(M):
    key, value = map(int, input().split(" "))
    graph[key].append(value)
    graph[value].append(key)

for i in range(1, len(graph)):
    graph[i].sort()

# DFS 함수 스택 구조 활용
def DFS(_graph, _start):
    visit = list()
    stack = list()

    stack.append(_start)

    while stack:

        # 스택의 우측 값(마지막 값)을 기준으로 탐색.
        node = stack.pop()

        if node not in visit:
            visit.append(node)

            if _graph[node] == None:
                return visit
            
            for i in range(len(_graph[node])-1, -1, -1):
                stack.append(_graph[node][i])

    return visit

# BFS 함수 collections의 deque를 통해 큐 구조 활용
def BFS(_graph, _start):
    visit = list()
    queue = deque()

    queue.append(_start)

    while queue:

        # 큐의 왼쪽 값을 기준으로 탐색.
        node = queue.popleft()

        if node not in visit:
                visit.append(node)

                if _graph[node] == None:
                    return visit

                queue.extend(_graph[node])

    return visit

# DFS 실행
for i in DFS(graph, V):
    print(i, end = " ")

print()

# BFS 실행
for i in BFS(graph, V):
    print(i, end = " ")