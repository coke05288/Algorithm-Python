
## 완전탐색
## Programmers 최소직사각형
## https://school.programmers.co.kr/learn/courses/30/lessons/86491

def solution(sizes):
    
    max_width = 0
    max_height = 0
    
    for width, height in sizes:
        if height > width:
            width, height = height, width
        if max_width < width:
            max_width = width
        if max_height < height:
            max_height = height
            
    return max_width * max_height


print(solution([[60, 50], [30, 70], [60, 30], [80, 40]]))
print(solution([[10, 7], [12, 3], [8, 15], [14, 7], [5, 15]]))

