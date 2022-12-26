## DFS & BFS
## 백준 14502 연구소
## https://www.acmicpc.net/problem/14502

from collections import deque
from sys import stdin
input = stdin.readline

N, M = map(int, input().split())

Graph = []

dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]

answer = 0

def bfs(Graph):
    q = deque()

    temp_graph = []

    for i in range(N):
        temp_list = []

        for j in range(M):
            temp_list.append(Graph[i][j])

        temp_graph.append(temp_list)
    
    for i in range(N):
        for j in range(M):
            if temp_graph[i][j] == 2:
                q.append((i, j))

    while q:
        x, y = q.popleft()
        
        for i in range(4):
            temp_x = x + dx[i]
            temp_y = y + dy[i]

            if temp_x < 0 or temp_x >= N or temp_y < 0 or temp_y >= M:
                continue
            else:
                if temp_graph[temp_x][temp_y] == 0:
                    temp_graph[temp_x][temp_y] = 2
                    q.append((temp_x, temp_y))

    cnt = 0

    for i in range(N):
        for j in range(M):
            if temp_graph[i][j] == 0:
                cnt += 1
    
    global answer

    answer = max(answer, cnt)


def solution(num):
    if num == 3:
        bfs(Graph)
        return
    
    for i in range(N):
        for j in range(M):
            if Graph[i][j] == 0:
                Graph[i][j] = 1
                solution(num+1)
                Graph[i][j] = 0
    
for _ in range(N):
    Graph.append(list(map(int, input().split())))

solution(0)

print(answer)