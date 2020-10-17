'''
백준 17142 연구실3

bfs, deque
itertools 조합, 체인
2차원 배열을 리스트화 > chain(*array)
'''

from collections import deque
from itertools import combinations as cb
from itertools import chain as chain

N,M = map(int, input().split())
labs = [list(map(int,input().split())) for _ in range(N)]

virus = []
for i in range(N):
    for j in range(N):
        if labs[i][j] == 2:
            virus.append([i,j])

d = [(0,-1),(0,1),(1,0),(-1,0)]

def bfs(virus_list):
    visited = [[-1]*N for _ in range(N)]
    q = deque()

    for i,j in virus_list:
        visited[i][j] = 0
        q.append([i,j])

    max_time = 0
    while q:
        i,j = q.popleft()
        for di,dj in d:
            ni = i+di
            nj = j+dj

            if not (0<=ni<N and 0<=nj<N):
                continue
            #방문 전이거나 벽이 아닌 곳 > 큐 삽입
            if visited[ni][nj] == -1 and labs[ni][nj] != 1:
                # 현 방문시점은 전 방문시점의 +1
                visited[ni][nj] = visited[i][j]+1
                # 방문 지역이 빈 곳이면 max타임 비교하기
                if labs[ni][nj] == 0:
                    max_time = max(max_time, visited[ni][nj])
                
                q.append([ni,nj])
    '''
    print("1-1: ", list(chain(*visited)))
    a = list(chain(*visited))
    print("1-2: ", a.count(-1))
    print("2-1: ", list(chain(*labs))) 
    b = list(chain(*labs))
    print("2-2: ", b.count(1))
    '''

    if list(chain(*visited)).count(-1) == list(chain(*labs)).count(1):
        answer.append(max_time)

cases = cb(virus,M)
answer = []

for case in cases:
    bfs(case)
print(min(answer) if answer else -1)