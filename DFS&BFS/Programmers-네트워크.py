## DFS & BFS
## Programmers 네트워크
## https://school.programmers.co.kr/learn/courses/30/lessons/43162

def dfs(v, computers):
    global visited
    
    visited[v] = True
    
    for i in range(len(computers[v])):
        if not visited[i] and computers[v][i] == 1:
            dfs(i, computers)

def solution(n, computers):
    global visited
    answer = 0
    
    visited = [False] * len(computers)
    
    for i in range(len(computers)):
        if not visited[i]:
            answer += 1
            dfs(i, computers)
    
    return answer

print(solution(3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]]	))
print(solution(3, [[1, 1, 0], [1, 1, 1], [0, 1, 1]]	))