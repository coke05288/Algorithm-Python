## DFS & BFS
## Programmers 타겟 넘버
## https://school.programmers.co.kr/learn/courses/30/lessons/43165

def dfs(numbers, target, depth, temp_sum):
    global cnt
    
    if depth == len(numbers):
        if temp_sum == target:
            cnt += 1
            return
        else:
            return
    
    dfs(numbers, target, depth + 1, temp_sum + numbers[depth])
    dfs(numbers, target, depth + 1, temp_sum - numbers[depth])

def solution(numbers, target):
    global cnt
    
    cnt = 0 
    
    dfs(numbers, target, 0, 0)
    
    return cnt

print(solution([1, 1, 1, 1, 1], 3))
print(solution([4, 1, 2, 1], 4))