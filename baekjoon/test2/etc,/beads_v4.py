'''
45653번 구슬 탈출4

BFS
'''

from collections import deque

N,M = map(int, input().split())
arr = [list(input()) for _ in range(N)]

#각 2개의 구슬 x,y좌표
visited = [[[[False]*M for _ in range(N)] for _ in range(M)] for _ in range(N)]

d = [(0,1),(0,-1),(1,0),(-1,0)]
q = deque()

def move(x,y,dx,dy):
    #이동한 칸 수
    count = 0

    #그 다음이 벽이 아닐 경우 & 구멍이 아닐 경우 > 계속 이동
    while arr[x+dx][y+dy] != '#' and arr[x][y] != 'O':
        x+=dx
        y+=dy
        count += 1
    return x,y,count

def bfs():
    while q:
        #red 구슬, blue 구슬
        rx,ry,bx,by,depth = q.popleft()

        for di,dj in d:
            red_nx, red_ny, red_count = move(rx,ry,di,dj)
            blue_nx, blue_ny, blue_count = move(bx,by,di,dj)

            #구멍에 떨어질 경우
            if arr[blue_nx][blue_ny] == 'O':
                continue
            #성공
            if arr[red_nx][red_ny] == 'O':
                print(depth+1)
                return
            
            #두 구슬은 같은 위치에 있을 수 없다
            if red_nx == blue_nx and red_ny == blue_ny:
                #움직인 거리가 많은 구슬이 한칸 뒤로 가기
                if red_count > blue_count:
                    red_nx -= di
                    red_ny -= dj

                else:
                    blue_nx -= di
                    blue_ny -= dj

            if not visited[red_nx][red_ny][blue_nx][blue_ny]:
                visited[red_nx][red_ny][blue_nx][blue_ny] = True
                q.append([red_nx,red_ny,blue_nx,blue_ny,depth+1])
    #실패
    print(-1)


for i in range(N):
    for j in range(M):
        if arr[i][j] == 'R':
            rx,ry = i,j
        elif arr[i][j] == 'B':
            bx,by = i,j

q.append([rx,ry,bx,by,0])
visited[rx][ry][bx][by] = True

bfs()