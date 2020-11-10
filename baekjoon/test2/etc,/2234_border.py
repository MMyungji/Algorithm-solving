'''
백준 2234번 성곽

BFS

1. 10진수 > 2진수 
        format(num,"b")   = 1011
        format(num, "#b") , bin(num) = 0b1011

2. 10진수에서 2진수로 바꾸면 
        <문자열>이 된다

3. 문자열 자리 수 맞추기, 빈 자리에 0으로 채우기 
        str.zfill(자리수)

4. 벽 하나를 제거했을 때, 나오는 최대 방의 크기?
        방을 구분하는 배열을 새로 만들어 비교하기
        같은 방이 아닐 때, 인접한 방끼리의 크기를 더해 max비교
'''

from collections import deque

M,N = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

#2진수로 바꾸기
for i in range(N):
    for j in range(M):
        arr[i][j] = format(arr[i][j], "b").zfill(4)

#남동북서
d = [(1,0),(0,1),(-1,0),(0,-1)]

# 가장 큰 방의 사이즈, 방의 개수, 벽하나 제외 시 가장 큰 방의 사이즈
max_size, how_many, max_of_max = 0,0,0

#방문 여부
visited = [[False]*M for _ in range(N)]

#방의 공간 분리 배열
rooms = [[0]*M for _ in range(N)]  
#방의 공간의 크기
room_size = []

# 방의 개수와 방의 크기 계산
def bfs(x,y,cnt):
    q = deque()

    q.append([x,y])
    size = 0

    while q:
        size += 1               #사이즈 업

        i,j = q.popleft()

        visited[i][j] = True    #방문 체크
        rooms[i][j] = cnt

        value = arr[i][j]       #벽의 유무를 나타내는 2진수
        move = []               #0이면 벽이 없으므로 움직일 수 있음 

        for v in range(4):
            if value[v] == '1':     #1이면 벽임으로 움직일 수 없음
                continue
            else:
                move.append(d[v])   #0이면 움직일 수 있음 > q에 추가
        
        for di,dj in move:
            nx = i+di
            ny = j+dj

            if visited[nx][ny] == False and [nx,ny] not in q:
                q.append([nx,ny])

    return size     #방의 사이즈 리턴, 최대 방의 크기와 비교

#방의 개수와 제일 큰 방의 크기 구하기 > bfs이용
for i in range(N):
    for j in range(M):
        if visited[i][j] == False:
            s = bfs(i,j,how_many)
            how_many+=1
        
            room_size.append(s)
            max_size = max(s, max_size)
            

print(how_many)
print(max_size)

#방 하나 제거시, 제일 큰 방의 크기 구하기
#방을 구분하는 배열을 만들고 그 배열을 이용해 인접한 방과의 크기 더하기
for i in range(N):
    for j in range(M):
        for di,dj in d:
            nx = i+di
            ny = j+dj
            if not (0<=nx<N and 0<=ny<M):
                continue
            if rooms[i][j] != rooms[nx][ny]:
                temp = room_size[rooms[i][j]] + room_size[rooms[nx][ny]]
                max_of_max = max(max_of_max, temp)

print(max_of_max)
