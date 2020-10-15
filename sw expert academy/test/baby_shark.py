import heapq

N = int(input())
fishes = [list(map(int, input().split())) for _ in range(N)]
                                  
shark_size = 2
ate = 0
answer = 0 

#상어 위치 찾기
for i in range(N):
    for j in range(N):
        if fishes[i][j] == 9:
            x,y = i,j
            fishes[i][j] = 0
            break
        
d = [(-1,0),(0,-1),(1,0),(0,1)]

def bfs(x,y,size):
    time = 0 # 물고기 먹는데 걸리는 시간
    queue = [(time, x, y)]  #방문할 위치
    visited = {(x,y)}       #방문한 좌표

    while queue:
        time,i,j = heapq.heappop(queue)
        if 0 < fishes[i][j] < size:
            fishes[i][j]=0
            return i,j,time
                                
        for di,dj in d:
            nx = x+di
            ny = y+dj
            time+=1
            if nx<0 or nx>=N or ny<0 or ny>=N:
                continue
            if fishes[nx][ny] <= size and (nx,ny) not in visited:
                visited.add((nx,ny))
                heapq.heappush(queue,(time,nx,ny))
        
    return x,y,0
'''
def bfs(si, sj, size):
    time = 0
    queue = [(time, si, sj)]
    visited = {(si, sj)}
    while queue:
        print(queue)
        for _ in range(len(queue)):
            time, i, j = heapq.heappop(queue)
            if 0 < fishes[i][j] < size:  # 자신보다 작으면 먹을 수 있다
                fishes[i][j] = 0
                return i, j, time  # 현재 좌표와 움직인 시간 반환

            for di, dj in [(-1, 0), (0, -1), (0, 1), (1, 0)]:
                if not (0 <= i+di < N and 0 <= j+dj < N):
                    continue
                if fishes[i+di][j+dj] <= size \
                        and (i+di, j+dj) not in visited:  # 자기보다 크면 지날 수 없다.
                    visited.add((i+di, j+dj))
                    heapq.heappush(queue, (time+1, i+di, j+dj))
        time += 1
        print(f"time up: {time}")
    return si, sj, 0  # 종료 조건, 움직이지 않은 상태
'''

#print(fishes)


#먹을 물고기가 있는 동안
#while True:
while True:
    #현재좌표와 움직인 시간
    x, y, time = bfs(x, y, shark_size)

    #더이상 움직이지 않으면 종료
    if time == 0:
        break

    #bfs한번 끝날때 마다 움직인 시간 더해주고 먹은 개수 올려주기
    answer+=time
    ate+=1

    #사이즈 늘려주기
    if ate == shark_size:
        shark_size+=1
        ate = 0

print(answer)