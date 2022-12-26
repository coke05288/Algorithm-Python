num_list = list(map(int, input().split()))


def solution(_num_list):
    
    answer = []
    count = [0] * max(_num_list)

    for i in _num_list:
        count[i-1] += 1

    for i in range(0, len(count)):
        if count[i] == max(count):
            answer.append(i+1)

    answer.sort(reverse=True)

    return answer


print(' '.join(map(str, solution(num_list))))