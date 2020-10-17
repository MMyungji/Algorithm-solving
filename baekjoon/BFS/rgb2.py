'''
백준 10026 적록색약
BFS, deque
좀더 깔끔하게 풀이
 > 방문 초기화
 > 컬러 확인은 함수 안에서
'''

from collections import deque

N = int(input())
grid = [list(input()) for _ in range(N)]

d = [(0,-1),(0,1),(1,0),(-1,0)]


def bfs(x,y):
    q = deque()
    q.append([x,y])
    color = grid[x][y]

    while q:
        i, j = q.popleft()
        visited[i][j] = True

        for di,dj in d:
            nx = i+di
            ny = j+dj

            if not (0<=nx<N and 0<=ny<N):
                continue
            if grid[nx][ny] == color and visited[nx][ny] == False and [nx,ny] not in q:
                q.append([nx,ny])

#정상적인 눈을 가진 사람
visited = [[False]*N for _ in range(N)]
original = 0

for i in range(N):
    for j in range(N):
        if not visited[i][j]:
            bfs(i,j)
            original+=1
print(original)

#적록색약
#visited 다시 초기화
visited = [[False]*N for _ in range(N)]
extra = 0

#"G" -> "R"
for i in range(N):
    for j in range(N):
        if grid[i][j] == "G":
            grid[i][j] = "R"

for i in range(N):
    for j in range(N):
        if not visited[i][j]:
            bfs(i,j)
            extra+=1


print(extra)

