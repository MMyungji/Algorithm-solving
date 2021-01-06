'''
백준 2151번 거울설치
'''

from collections import deque

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def bfs(x, y, dir):
    q.append([x, y, dir])
    visited[x][y][dir] = 1
    ans = []
    while q:
        x, y, dir = q.popleft()
        nx = x + dx[dir]
        ny = y + dy[dir]
        if 0 <= nx < n and 0 <= ny < n:
            if not visited[nx][ny][dir] or visited[nx][ny][dir] > visited[x][y][dir]:
                if a[nx][ny] != '*':
                    visited[nx][ny][dir] = visited[x][y][dir]
                    if nx == fx and ny == fy:
                        ans.append(visited[nx][ny][dir])
                        continue
                    q.append([nx, ny, dir])
                    if a[nx][ny] == '!':
                        #90도 방향전환
                        ndir = [(dir+1) % 4, (dir+3) % 4]
                        for d in ndir:
                            if not visited[nx][ny][d] or visited[nx][ny][d] > visited[nx][ny][dir] + 1:
                                visited[nx][ny][d] = visited[nx][ny][dir] + 1
                                q.append([nx, ny, d])

    #최소값 출력
    print(min(ans)-1)

n = int(input())
q = deque()
visited = [[[0]*4 for _ in range(n)] for _ in range(n)]

a, temp = [], []
for i in range(n):
    row = list(input().strip())
    a.append(row)
    for j in range(n):
        if row[j] == '#':
            temp.extend([i, j])
sx, sy, fx, fy = temp

for i in range(4):
    nx = sx + dx[i]
    ny = sy + dy[i]
    if 0 <= nx < n and 0 <= ny < n:
        if a[nx][ny] != '*':
            dir = i
            break

bfs(sx, sy, dir)