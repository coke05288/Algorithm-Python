## Divide & Conquer
## Baekjoon 2447 별찍기 10
## https://www.acmicpc.net/problem/2447

def draw_stars(n):

    if n == 1:
        return ["*"]
    
    stars = draw_stars(n//3)
    line = []

    for star in stars:
        line.append(star * 3)
    for star in stars:
        line.append(star + ' ' * (n//3) + star)
    for star in stars:
        line.append(star * 3)
    
    return line
    
N = int(input())

print('\n'.join(draw_stars(N)))
