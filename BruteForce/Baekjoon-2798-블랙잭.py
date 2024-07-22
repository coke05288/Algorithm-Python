## Brute Force
## Baekjoon 2798 블랙잭
## https://www.acmicpc.net/problem/2798

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
card_list = list(map(int, input().split()))
answer = 0

for i in range(N):
    for j in range(i + 1, N):
        for k in range(j + 1, N):
            temp = card_list[i] + card_list[j] + card_list[k]
            # print(f"@@ {i}/{j}/{k} temp : {temp}")
            if temp > M: 
                # print(f"@@ continue")
                continue
            else:
                if temp > answer:
                    answer = temp
                    # print(f"@@ answer : {answer}")

print(answer)