'''
백준 14238번 출근기록
: 조건에 맞는 출근기록인지 확인

dp문제
 : [A][B][C][전전날][전날]
'''
from sys import stdin

#dp[A][B][C][전전날][전날]
def dfs(a, b, c, prev):
    # a, b, c의 개수가 초기 카운트와 같으면 찾은 것
    if [a, b, c] == cnt:
        print(''.join(answer))
        exit(0)

    if dp[a][b][c][prev[0]][prev[1]]:
        return False

    dp[a][b][c][prev[0]][prev[1]] = True

    # A개수 만큼 사용하지 않았다면
    if a + 1 <= cnt[A]:
        answer[a + b + c] = 'A'
        if dfs(a + 1, b, c, [prev[1], A]):
            return True
    # B개수 만큼 사용하지 않았다면
    if b + 1 <= cnt[B]:
        answer[a + b + c] = 'B'
        # 전날에 선택한 것이 B가 아니라면
        if prev[1] != B:
            if dfs(a, b + 1, c, [prev[1], B]):
                return True
    # C개수 만큼 사용하지 않았다면
    if c + 1 <= cnt[C]:
        answer[a + b + c] = 'C'
        # 전전날과 전날에 선택한 것이 C가 아니라면
        if prev[0] != C and prev[1] != C:
            if dfs(a, b, c + 1, [prev[1], C]):
                return True
    return False

s = list(stdin.readline().rstrip())
length = len(s)
answer = [''] * length

#cnt수를 구별하기 위한 상수
A, B, C = 0, 1, 2
# a, b, c 개수 카운트.
cnt = [s.count(word) for word in ('A', 'B', 'C')]

#5차원 배열 생성
#dp[A][B][C][전전날][전날]
dp = [[[[[False for _ in range(3)] for _ in range(3)] for _ in range(
    length)] for _ in range(length)] for _ in range(length)]
dfs(0, 0, 0, [0, 0])
print(-1)
