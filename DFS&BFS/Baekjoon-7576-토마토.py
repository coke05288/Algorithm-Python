## DFS & BFS
## Baekjoon 7576 토마토
## https://www.acmicpc.net/problem/7576

from collections import deque

import sys
input = sys.stdin.readline

M, N = map(int, input().split())

box = [list(map(int, input().split())) for _ in range(N)]

def bfs(box, queue):
    
    direction = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    while queue:
        y, x = queue.popleft()
        
        for dy, dx in direction:
            nx, ny = x + dx, y + dy
            if ny >= 0 and ny < N and nx >= 0 and nx < M :
                if box[ny][nx] == 0:
                    box[ny][nx] = box[y][x] + 1
                    queue.append((ny, nx))


def solution(M, N, box):

    queue = deque()
    
    for i in range(N):
        for j in range(M):
            if box[i][j] == 1:
                queue.append((i, j))

    bfs(box, queue)

    temp_max = 0

    for i in range(N):
        for j in range(M):
            if box[i][j] == 0:
                return -1
            
            temp_max = max(temp_max, box[i][j])

    return temp_max - 1

print(solution(M, N, box))