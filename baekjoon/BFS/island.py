'''
백준 4963 섬의 개수
bfs, deque 
변수 조건 확인 하기
'''

from collections import deque

d = [(1,0),(-1,0),(0,1),(0,-1),(-1,-1),(-1,1),(1,1),(1,-1)]

def bfs(x,y):
    q = deque()
    q.append([x,y])

    while q:
        i,j = q.popleft()
        maps[i][j] = 0

        for di,dj in d:
            nx = i+di
            ny = j+dj

            if not (0<=nx<M and 0<=ny<N):
                continue

            if maps[nx][ny] == 1 and [nx,ny] not in q:
                q.append([nx,ny])

def find_island(m):
    island_num = 0
    for i in range(M):
        for j in range(N):
            if m[i][j] == 1:
                bfs(i,j)
                island_num += 1

    return island_num

while True:
    N, M = map(int, input().split())
    if N==0 and M==0:
        break 

    maps = [list(map(int,input().split())) for _ in range(M)]
    
    print(find_island(maps))





