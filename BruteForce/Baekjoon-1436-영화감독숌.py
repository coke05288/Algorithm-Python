## Brute Force
## Baekjoon 1436 영화감독 숌
## https://www.acmicpc.net/problem/1436

import sys
input = sys.stdin.readline

N = int(input())
idx = 0
fin_num = 666

def check_fin_num(num):
    cnt = 0
    prev = 0
    
    for i in list(str(num)):
        if prev == '6' and i == '6':
            cnt += 1
        else:
            cnt = 0

        prev = i
        
        if cnt >= 2:
            return True

    return False


while True:
    if check_fin_num(fin_num):
        idx += 1

    if N == idx:
        print(fin_num)
        break

    fin_num += 1
