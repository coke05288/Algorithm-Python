## 구현(Implementation)
## Baekjoon 1259 펠린드롬수
## https://www.acmicpc.net/problem/1259

while True:
    case = input()
    if case != "0":
        case = list(map(int, case))
        start, end = 0, len(case)-1
        for i in range(len(case)//2 + 1):
            start += i
            end -= i
            if case[start] == case[end]:
                if start >= end:
                    print("yes")
                    break
                continue
            else:
                print("no")
                break
    else:
        break