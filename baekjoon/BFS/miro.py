'''
2178번 미로 탐색
최단거리 구하는 문제 : BFS 사용
'''
from collections import deque
import sys

N,M = map(int,sys.stdin.readline().split())
miro = [list(map(int,sys.stdin.readline().rstrip())) for _ in range(N)]

d = [(0,-1), (0,1), (1,0), (-1,0)]

queue =  deque([(0,0)])
distance  = [[0]*M for _ in range(N)] #방문 기록을 리스트로 나타내면 시간초과가 생김  >  배열로 체크
distance[0][0] = 1

while queue:
    i, j = queue.popleft()

    for di, dj in d:
        nx = i+di
        ny  = j+dj
        if not (0<=nx<N and 0<=ny<M):
            continue
        if miro[nx][ny] == 1 and distance[nx][ny] == 0:
            queue.append((nx,ny))
            distance[nx][ny] = distance[i][j]+1

print(distance[N-1][M-1])







