## 구현(Implementation)
## Baekjoon 2577 숫자의 개수
## https://www.acmicpc.net/problem/2577

A = int(input())
B = int(input())
C = int(input())

mul_num = list(map(int, str(A*B*C)))
result = [0 for i in range(10)]

for i in mul_num :
    result[i]+=1

for i in result:
    print(i)