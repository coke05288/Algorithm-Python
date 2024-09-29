## DFS & BFS
## Programmers 아이템 줍기
## https://school.programmers.co.kr/learn/courses/30/lessons/87694?language=python3

from collections import deque

def solution(rectangle, characterX, characterY, itemX, itemY):
    answer = 0

    graph = [[-1 for _ in range(102)] for _ in range(102)] 
    visited = [[1 for _ in range(102)] for _ in range(102)] 
    direction = [(1, 0), (0, 1), (-1, 0), (0, -1)]

    queue = deque()

    for item in rectangle: 
        left_top = (item[0] * 2, item[1] * 2)
        right_bot = (item[2] * 2, item[3] * 2)

        for i in range(left_top[0], right_bot[0] + 1):
            for j in range(left_top[1], right_bot[1] + 1):
                if left_top[0] < i < right_bot[0] and left_top[1] < j < right_bot[1]:
                    graph[i][j] = 0
                elif graph[i][j] != 0:
                    graph[i][j] = 1

    cx, cy = characterX * 2, characterY * 2
    ix, iy = itemX * 2, itemY * 2

    queue.append((cx, cy))

    while queue:

        x, y = queue.popleft()

        if x == ix and y == iy:
            answer = visited[x][y] // 2
            break

        for dr in direction:
            nx, ny = x + dr[0], y + dr[1]

            if graph[nx][ny] == 1 and visited[nx][ny] == 1:
                visited[nx][ny] += visited[x][y]
                queue.append((nx, ny))

    return answer


print(solution([[1,1,7,4],[3,2,5,5],[4,3,6,9],[2,6,8,8]], 1, 3, 7, 8)) # 17
print(solution([[1,1,5,7]], 1, 1, 4, 7))                               # 9
print(solution([[2,1,7,5],[6,4,10,10]], 3, 1, 7, 10))                  # 15
print(solution([[2,2,5,5],[1,3,6,4],[3,1,4,6]], 1, 4, 6, 3))           # 10
print(solution([[1,1,8,4],[2,2,4,9],[3,6,9,8],[6,3,7,7]], 9, 7, 6, 1)) # 11