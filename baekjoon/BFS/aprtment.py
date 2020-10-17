'''
백준 2667 단지번호붙이기
bfs 사용, 큐 deque, 큐에 중복으로 들어가지 않도록 주의하기
'''
from collections import deque

N = int(input())
town = [list(map(int,input())) for _ in range(N)]

d = [(0,1),(0,-1),(1,0),(-1,0)]
apt = 0
apt_list = []

def bfs(i,j):
    q = deque()
    q.append([i,j])
    apt_num = 0

    while q:
        #print(q)
        x, y = q.popleft()
        town[x][y] = 0
        apt_num+=1
        #print(apt_num)

        for di,dj in d:
            nx = x+di
            ny = y+dj

            if not (0<=nx<N and 0<=ny<N):
                continue
            if town[nx][ny] == 1 and [nx,ny] not in q:
                q.append([nx,ny])

                
            
    return apt_num
                


for i in range(N):
    for j in range(N):
        if town[i][j] == 1:
            #print(f"i, j = [{i} {j}]")
            #print("bfs 결과 : ", bfs(i,j))
            apt_list.append(bfs(i,j))
            apt+=1

apt_list.sort()
print(apt)
for i in apt_list:
    print(i)



    