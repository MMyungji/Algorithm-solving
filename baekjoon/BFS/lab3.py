'''
백준 17142 연구실3

bfs, deque
itertools 조합

[[시간초과]]
'''

from collections import deque
from itertools import combinations as cb
from copy import deepcopy as dc
import math

d = [(1,0),(-1,0),(0,1),(0,-1)]

N, M = map(int, input().split())

labs = [list(map(int,input().split())) for _ in range(N)]

#바이러스 찾아서 리스트안에 넣기
virus = []
for i in range(N):
    for j in range(N):
        if labs[i][j] == 2:
            #위치와 바이러스 퍼진 시점 저장
            #바이러스 자체여서 시점은 0
            virus.append([i,j,0])


    

#연구실과 바이러스 경우의 수 
#경우의 수 대로 확인하기
def bfs(labs,case):
    q = deque()
    visited = [[0]*N for _ in range(N)]

    lab = dc(labs)

    #바이러스 시작 점, 큐에 저장
    q.extend(case)

    #마지막으로 바이러스가 퍼진 시점 구하기
    last_change = 0
    while q:
        i,j,count = q.popleft()
        visited[i][j] = 1

        for di,dj in d:
            nx = i+di
            ny = j+dj

            if not (0<=nx<N and 0<=ny<N):
                continue
            #방문하지 않고 벽이 아닌 곳(빈 공간인 곳)
            if visited[nx][ny] == 0 and lab[nx][ny] != 1:
                #방문 했다는 표시
                visited[i][j] = 1
                #만약 그 곳이 빈 공간이라면
                if lab[nx][ny] == 0:
                    #바이러스 퍼짐
                    lab[nx][ny] = 2
                    #바이러스가 마지막으로 퍼진 시점
                    last_change = count+1
                
                q.append([nx,ny,count+1])
    
    #마지막에 체크
    if check(lab) == 0:
        return last_change
    else:
        return -1
    
    
    
#모든 빈 곳에 바이러스가 버졌는지 확인하기
def check(lab):
    for i in range(N):
        for j in range(N):
            if lab[i][j] == 0:
                return -1

    return 0



#양의 무한대
mins = math.inf

#모든 조합
active = cb(virus,M)
#모든 경우의 수 대입
for case in active:
    result = bfs(labs,case)
    #바이러스가 모든 곳에 퍼졌고, 그 중 최소 구하기
    if result != -1 and mins > result:
        mins = result

if mins == math.inf:
    print(-1)
else:
    print(mins)
