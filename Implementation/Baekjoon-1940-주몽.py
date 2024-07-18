## 구현(Implementation), 투포인터(Two-Pointer)
## Baekjoon 1940 주몽
## https://www.acmicpc.net/problem/1940

import sys
input = sys.stdin.readline

N = int(input())
M = int(input())

mat_nums = list(map(int, input().split()))
mat_nums.sort()

answer = 0

s = 0
e = N - 1

while s < e:
    if mat_nums[s] + mat_nums[e] < M:
        s += 1 
    elif mat_nums[s] + mat_nums[e] > M:
        e -= 1
    else:
        answer += 1
        s += 1 
        e -= 1
        

print(answer)