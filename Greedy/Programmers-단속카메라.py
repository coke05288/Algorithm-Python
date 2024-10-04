## 그리디 알고리즘
## 프로그래머스 단속카메라
## https://school.programmers.co.kr/learn/courses/30/lessons/42884#

def solution(routes):
    answer = 0
    
    routes.sort(key = lambda x : x[1])
    
    spot = -30001
    
    for route in routes:
        if route[0] > spot:
            answer += 1
            spot = route[1]
                
    return answer

print(solution([[-20,-15], [-14,-5], [-18,-13], [-5,-3]]	))