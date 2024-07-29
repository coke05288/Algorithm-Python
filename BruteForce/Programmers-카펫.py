
## 완전탐색
## Programmers 카펫
## https://school.programmers.co.kr/learn/courses/30/lessons/42842

def solution(brown, yellow):
    
    measures = []
    
    for i in range(1, yellow + 1):
        if yellow % i == 0:
            measures.append(i)
    
    s = 0
    e = len(measures) - 1
    
    while s < e:
        if measures[s] * 2 + measures[e] * 2 + 4 == brown:
            break
        else:
            s += 1
            e -= 1
        
    
    return [measures[e] + 2, measures[s] + 2]


print(solution(10, 2))
print(solution(8, 1))
print(solution(24, 24))

