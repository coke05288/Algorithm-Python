## 그리디 알고리즘
## 백준 14916 거스름돈
## https://www.acmicpc.net/problem/14916

N = int(input())

def solution(N):
    temp_count = 0
    clear = False

    if N % 5 == 0:
        return N // 5
    else:
        while N >= 0:
            if N % 5 == 0:
                clear = True
                return N // 5 + temp_count

            temp_count += 1
            N -= 2
        
        if not clear:
            return -1

print(solution(N))
