## 구현(Implementation), 슬라이딩 윈도우
## Baekjoon 29700 우당탕탕 영화예매
## https://www.acmicpc.net/problem/29700

N, M, K = map(int, input().split())
seats = []

for _ in range(N):
    seats.append(list(input().strip()))

def solution(N, M, K, seats):
    answer = 0

    for i in range(N):
        for j in range(M):
            if seats[i][j] == '0':
                check = True
                for k in range(K):
                    if j + k < M:
                        if seats[i][j + k] != '0':
                            check = False
                    else:
                        check = False
                if check:
                    answer += 1

    return answer

print(solution(N, M, K, seats))