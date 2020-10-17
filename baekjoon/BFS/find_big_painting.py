'''
백준 1926 그림 문제
bfs, deque이용
'''

from collections import deque

N, M = map(int, input().split())

museum = [list(map(int,input().split())) for _ in range(N)]

d = [(1,0), (-1,0),(0,1),(0,-1)]
def bfs(x,y):
    q = deque()
    q.append([x,y])

    size = 0

    while q:
        i, j = q.popleft()
        museum[i][j] = 0
        size += 1


        for di,dj in d:
            nx = i+di
            ny = j+dj

            if not (0<=nx<N and 0<=ny<M):
                continue
            if museum[nx][ny] == 1 and [nx,ny] not in q:
                q.append([nx,ny])

    return size

size_list = []
count = 0
for i in range(N):
    for j in range(M):
        if museum[i][j] == 1:
            paint = bfs(i,j)
            size_list.append(paint)
            count += 1

print(count)
if size_list:
    print(max(size_list))
else:
    print(0)
