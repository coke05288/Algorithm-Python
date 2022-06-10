
## 그리디 알고리즘
## 백준 11399 ATM

n = int(input())
P = list(map(int, input().split(" ")))

def total_sum(_P):
    answer = 0

    for i in _P:
        answer += i
    
    return answer

P.sort()

for i in range(1, len(P)):
    answer = P[i-1] + P[i]
    P[i] = answer

print(total_sum(P))