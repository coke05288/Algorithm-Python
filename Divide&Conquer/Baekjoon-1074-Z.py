import sys
input = sys.stdin.readline

N, r, c = map(int, input().split())


def z_search(N, r, c):
    if N == 0:
        return 0

    # 2 * (r % 2) + (c % 2) : 2 * 2 블록에서 r, c가 몇 사분면에 있는지에 대한 연산
    # 4 * z_search(N - 1, r // 2, c // 2) : 하위 문제는 상위 문제의 1/4 만큼 줄어들기 때문에
    return 2 * (r % 2) + (c % 2) + 4 * z_search(N - 1, r // 2, c // 2)

print(z_search(N, r, c))
