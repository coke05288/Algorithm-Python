## 해시
## 프로그래머스 폰켓몬
## https://school.programmers.co.kr/learn/courses/30/lessons/1845

def solution(nums):
    return int(min(len(nums)/2, len(set(nums))))

print(solution([3,1,2,3]))
print(solution([3,3,3,2,2,4]))
print(solution([3,3,3,2,2,2]))