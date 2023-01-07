## 구현(Implementation)
## Baekjoon 12933 오리
## https://www.acmicpc.net/problem/12933

def solution():
    result = 0
    
    duck = ['k', 'c', 'a', 'u', 'q']

    while sound:
        check = False

        for i in range(len(sound)):
            if sound[i] == duck[-1]:
                sound[i] = 'z'
                duck.pop()
            
            if not duck:
                duck = ['k', 'c', 'a', 'u', 'q']
                check = True
        
        if 'z' in sound and len(duck) == 5:
            delete_z(sound)

            if check :
                result += 1
            
            duck = ['k', 'c', 'a', 'u', 'q']
        else:
            result = 0
            break

    if result > 0:
        return result
    else:
        return -1

def delete_z(_list):
    
    temp_list = _list
    
    while 'z' in temp_list:
        temp_list.remove('z')

    return temp_list

sound = list(input())
print(solution())