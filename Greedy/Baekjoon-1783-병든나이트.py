## 그리디 알고리즘
## 백준 1783 병든 나이트
## https://www.acmicpc.net/problem/1783

N, M = map(int, input().split(" "))

if N == 1:
    print(1)
elif N == 2:
    print(1 + min(3, (M-1)//2))
elif M < 7:
    print(1 + min(3, M-1))
else :
    print(1 + 2 + M - 5)