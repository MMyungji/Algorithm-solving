'''
백준 14442번 벽 부수고 이동하기 2

1. bfs - 최단거리 구하기 , 방문여부 확인
2. 부실 수 있는 벽은 최대 k개
    : 경우의 수가 많음
    : 부신 벽의 경우의 수도 방문여부 확인에 같이 체크하기
    : [x좌표][y좌표][벽 부순 횟수]
3. 시간초과
    : 입력 라이브러리 변경
   from sys import stdin 
   stdin.readline()
'''
from collections import deque
from sys import stdin

d = [[0,1],[0,-1],[1,0],[-1,0]]
n,m,k = map(int,stdin.readline().split())
arr = [list(map(int,stdin.readline().strip())) for _ in range(n)]

#방문 체크와 이동거리 저장
#k+1 : 벽을 안부신 것부터 k개 부신 것까지
#[x좌표][y좌표][벽 부순 횟수] = 이동거리
dist = [[[0]*(k+1) for _ in range(m)] for _ in range(n)]

def bfs():       
    q = deque()
    q.append([0,0,0])

    dist[0][0][0] = 1

    while q:
        x,y,w = q.popleft()
        
        if x == n-1 and y == m-1:
            return dist[x][y][w]
        
        for di,dj in d:
            nx = di+x
            ny = dj+y
            nw = w+1

            if not (0<=nx<n and 0<=ny<m):
                continue
            if dist[nx][ny][w]:
                continue
            
            #벽이 없으면 방문만 체크
            if arr[nx][ny] == 0:
                dist[nx][ny][w] = dist[x][y][w] + 1
                q.append([nx,ny,w])

            #벽이 있으면 w+1(nw)로
            if arr[nx][ny] == 1 and nw<=k:
                dist[nx][ny][nw] = dist[x][y][w] + 1
                q.append([nx,ny,nw])
    #없는 경우
    return -1

print(bfs())