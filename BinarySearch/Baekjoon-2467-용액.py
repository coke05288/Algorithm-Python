## BinarySearch
## Baekjoon 2467 용액
## https://www.acmicpc.net/problem/2467

import sys
input = sys.stdin.readline

N = int(input())
values = list(map(int, input().split()))

s = 0   
e = len(values) - 1

diff_zero = abs(values[s] + values[e])

answer_s = s
answer_e = e

while s < e:
    
    mix_value = values[s] + values[e]

    if abs(diff_zero) >= abs(mix_value):
        diff_zero = abs(mix_value)
        answer_s = s
        answer_e = e
        
        if diff_zero == 0:
            break

    if mix_value > 0:
        e -= 1
    elif mix_value < 0 :
        s += 1

print(values[answer_s], values[answer_e])