'''
백준 10026 적록색약
BFS, deque

'''
from collections import deque
from copy import deepcopy as dc

N = int(input())
grid = [list(input()) for _ in range(N)]

d = [(0,1), (0,-1), (1,0), (-1,0)]
def bfs(x,y,color,grid,visited):
    q = deque()
    q.append([x,y])

    while q:
        i,j = q.popleft()
        visited[i][j] = True
        grid[i][j] = 0

        for di,dj in d:
            nx = i+di
            ny = j+dj

            if not (0<=nx<N and 0<=ny<N):
                continue
            if grid[nx][ny] == color and visited[nx][ny] == False and [nx,ny] not in q:
                q.append([nx,ny])


grid2 = dc(grid)
visited2 = [[False]*N for _ in range(N)]
original = 0

grid3 = dc(grid)
for i in range(N):
    for j in range(N):
        if grid3[i][j] == "R" or grid3[i][j] == "G":
            grid3[i][j] = "RG"
extra = 0
visited3 = [[False]*N for _ in range(N)]

for i in range(N):
    for j in range(N):
        if grid2[i][j] == "R":
            #print("빨강지역")
            bfs(i,j,"R",grid2,visited2)
            original += 1
        if grid2[i][j] == "G":
            #print("초록지역")
            bfs(i,j,"G",grid2,visited2)
            original += 1
        if grid2[i][j] == "B":
            #print("파란지역")
            bfs(i,j,"B",grid2,visited2)
            original += 1

for i in range(N):
    for j in range(N):        
        if grid3[i][j] == "RG":
            #print("3.모호지역")
            bfs(i,j,"RG",grid3,visited3)
            extra += 1
        if grid3[i][j] == "B":
            #print("3.파랑지역")
            bfs(i,j,"B",grid3,visited3)
            extra += 1
print(original)
print(extra)




