'''
16236 백준 아기 상어
우선순위 조건 있음 : heapq
우선순위 조건 순대로 삽입하기

 - 이 문제의 경우 거리순으로
 heappush(q,(distance, x, y))
'''
import heapq

d = [(1,0),(0,-1),(1,0),(-1,0)]

def bfs(x,y):
    q = []
    visited = [[0]*N for _ in range(N)]

    sea[x][y] = 0
    #좌표 + 시간
    heapq.heappush(q,(0,x,y))

    size = 2    #상어 사이즈
    count = 0   #물고기 먹은 수
    time = 0    #걸린 시간

    while q:
        d,i,j = heapq.heappop(q)
        print(f"{i} {j}")

        if 0 < sea[i][j] < size:    #방문한 곳의 물고기 사이즈가 상어 사이즈보다 작으면 먹기
            print(f"물고기 먹음 {i} {j}")
            count+=1
            sea[i][j] = 0
            time += d

            if size == count:       #상어의 사이즈 만큼 먹었다면 상어의 사이즈 업
                size+=1
                count = 0

            d = 0
            q = []
            visited = [[0]*N for _ in range(N)]
        
        for di, dj in (0,-1),(-1,0),(1,0),(0,1):
            nx = i+di
            ny = j+dj
            nd = d+1

            if not (0<=nx<N and 0<=ny<N):
                continue
            if sea[nx][ny] > size:
                continue
            if visited[nx][ny] == 1:
                continue
            
            visited[nx][ny] = 1
            heapq.heappush(q,(nd,nx,ny))
                

    print(time)


N = int(input())
sea = [list(map(int,input().split())) for _ in range(N)]

for i in range(N):
    for j in range(N):
        if sea[i][j] == 9:
            bfs(i,j)
            
