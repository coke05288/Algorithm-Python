## DFS & BFS
## Programmers 게임맵최단거리
## https://school.programmers.co.kr/learn/courses/30/lessons/1844?language=python3

from collections import deque

def solution(maps):
    queue = deque()    
    queue.append((0, 0))

    direction = [(1, 0), (0, 1), (-1, 0), (0, -1)]

    while queue:
        y, x = queue.popleft()

        for dy, dx in direction:
            ny, nx = y + dy, x + dx

            if nx >= 0 and ny >= 0 and nx < len(maps[0]) and ny < len(maps):
                if maps[ny][nx] == 1:
                    queue.append((ny, nx))
                    maps[ny][nx] += maps[y][x]
        

    if maps[-1][-1] < 2:
        return -1

    return maps[-1][-1]

print(solution([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]]))
print(solution([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,0],[0,0,0,0,1]]))

