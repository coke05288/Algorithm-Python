## 구현(Implementation)
## Baekjoon 1205 등수구하기
## https://www.acmicpc.net/problem/1205

n, point, p = map(int, input().split())

if n == 0 : print(1)
else:
    ranking_list = list(map(int, input().split()))
    if n == p and point <= ranking_list[-1]:
        print(-1)
    else:
        rank = n + 1
        for i in range(len(ranking_list)):
            if ranking_list[i] <= point:
                rank = i + 1
                break
        print(rank)

