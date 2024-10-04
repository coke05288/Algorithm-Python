## 그리디 알고리즘
## MST(최소신장트리), Kruskal 알고리즘
## 프로그래머스 섬 연결하기
## https://school.programmers.co.kr/learn/courses/30/lessons/42861

def solution(n, costs):
    global parents
    answer = 0
    
    connect = set([costs[0][0]])
    costs.sort(key = lambda x : x[2])
    
    while len(connect) != n:
        for cost in costs:
            if cost[0] in connect and cost[1] in connect:
                continue
            
            if cost[0] in connect or cost[1] in connect:
                connect.update([cost[0], cost[1]])
                print(connect)
                answer += cost[2]
                break
    
    return answer

print(solution(4, [[0,1,1],[0,2,2],[1,2,5],[1,3,1],[2,3,8]]))