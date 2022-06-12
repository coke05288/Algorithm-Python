## Brute Force
## Baekjoon 2702 숫자판 점프
## https://www.acmicpc.net/problem/2702

def lcm(_a, _b):
    return _a *_b//gcd(_a, _b)

def gcd(_a, _b):
    if _b == 0:
        return _a
    else:
        return gcd(_b, _a%_b)

T = int(input())

for i in range(T):
    
    a, b = map(int, input().split())

    print(lcm(a, b), gcd(a, b))
