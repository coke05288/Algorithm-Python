## 슬라이딩 윈도우
## Baekjoon 12891 DNA 비밀번호구하기
## https://www.acmicpc.net/problem/12891

import sys
input = sys.stdin.readline

S, P = map(int, input().split())
DNA = list(input().rstrip())

check_dna = [0] * 4
window_dna = [0] * 4

check_dna = list(map(int, input().split()))

result = 0
check_result = 0

def window_add(x):
    global check_dna, window_dna, check_result

    if x == 'A':
        window_dna[0] += 1
        if check_dna[0] == window_dna[0]:
            check_result += 1
    elif x == 'C':
        window_dna[1] += 1
        if check_dna[1] == window_dna[1]:
            check_result += 1
    elif x == 'G':
        window_dna[2] += 1
        if check_dna[2] == window_dna[2]:
            check_result += 1
    elif x == 'T':
        window_dna[3] += 1
        if check_dna[3] == window_dna[3]:
            check_result += 1

def window_remove(x):
    global check_dna, window_dna, check_result

    if x == 'A':
        if check_dna[0] == window_dna[0]:
            check_result -= 1
        window_dna[0] -= 1
    elif x == 'C':
        if check_dna[1] == window_dna[1]:
            check_result -= 1
        window_dna[1] -= 1
    elif x == 'G':
        if check_dna[2] == window_dna[2]:
            check_result -= 1
        window_dna[2] -= 1
    elif x == 'T':
        if check_dna[3] == window_dna[3]:
            check_result -= 1
        window_dna[3] -= 1

for i in range(4):
    if check_dna[i] == 0:
        check_result += 1

for i in range(P):
    window_add(DNA[i])

if check_result == 4:
    result += 1

for i in range(P, S):
    
    j = i - P

    window_add(DNA[i])
    window_remove(DNA[j])
    
    if check_result == 4:
        result += 1

print(result)