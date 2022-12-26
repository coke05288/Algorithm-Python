
def check_intersection(line_1, line_2):
    A, B, E = line_1
    C, D, F = line_2

    if A*D - B*C == 0:
        return None
    
    X = (B*F - E*D) / (A*D - B*C)
    Y = (E*C - A*F) / (A*D - B*C)

    if X == int(X) and Y == int(Y):
        return (int(X), int(Y))


def solution(line):
    answer = []
    points = set()

    # 직선들의 정수 교점 구하기
    for i in range(0, len(line)):
        for j in range(i+1, len(line)):
            point = check_intersection(line[i], line[j])
            
            if point:
                points.add(point)

    # 그래프 초기화
    X_points = [point[0] for point in points]
    Y_points = [point[1] for point in points]

    X_min = min(X_points)
    Y_min = min(Y_points)
    X_max = max(X_points)
    Y_max = max(Y_points)

    answer = ['.' * (X_max - X_min + 1)] * (Y_max - Y_min + 1)

    # 교점 그리기
    for point in points:
        temp_x, temp_y = point

        answer[Y_max - temp_y] = answer[Y_max - temp_y][:temp_x - X_min] + "*" + answer[Y_max - temp_y][temp_x - X_min + 1:]

    return answer


print(solution([[2, -1, 4], [-2, -1, 4], [0, -1, 1], [5, -8, -12], [5, 8, 12]]))

print(solution([[0, 1, -1], [1, 0, -1], [1, 0, 1]]))

print(solution([[1, -1, 0], [2, -1, 0]]))