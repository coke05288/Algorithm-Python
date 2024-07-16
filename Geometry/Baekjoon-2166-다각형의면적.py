## 기하학(Geometry)
## Baekjoon 4153 직각삼각형
## https://www.acmicpc.net/problem/4153

def check_tri(tri):

    if tri[2]**2 == tri[0]**2 + tri[1]**2:
        return True
    else:
        return False


while True:
    a, b, c = map(int, input().split())

    if a == 0 and b == 0 and c ==0 : 
        break

    if check_tri(sorted([a, b, c])):
        print("right")
    else:
        print("wrong")