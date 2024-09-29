## DFS & BFS
## Programmers 단어변환
## https://school.programmers.co.kr/learn/courses/30/lessons/43163

from collections import deque

def solution(begin, target, words):
    answer = 0

    visited = [False for _ in range(len(words))]
    queue = deque()
    queue.append([begin, 0])

    while queue:
        word, cnt = queue.popleft()
        
        if word == target:
            answer = cnt
            break

        for i in range(len(words)):
            temp_cnt = 0
            if not visited[i]:
                for j in range(len(word)):
                    if words[i][j] != word[j]:
                        temp_cnt += 1
                if temp_cnt == 1:
                    queue.append([words[i], cnt + 1])
                    visited[i] = True
    
    return answer


print(solution("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"])) # 4
print(solution("hit", "cog", ["hot", "dot", "dog", "lot", "log"])) # 0