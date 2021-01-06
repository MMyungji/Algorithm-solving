'''
백준 15685번 드래곤 커브

브루트포스

1. x,y가 행열의 반대
    x = 열
    y = 행
2. 규칙
    시계 방향으로 회전 > 실제 문제풀땐 반시계로 적용함
    1) 다음 이동 방향 = (현재 이동 방향 + 1) % 4
    2) 세대별, 이동방향 순서 = 반대순서로
'''
import sys

dir = [[1,0],[0,-1],[-1,0],[0,1]]

input = sys.stdin.readline
n = int(input())
a = [[0]*101 for _ in range(101)]

for _ in range(n):
    x,y,d,g = map(int,input().split())
    a[x][y] = 1
    move = [d]
    for _ in range(g):
        tmp = []
        for i in range(len(move)):
            tmp.append((move[-1-i]+1)%4)
        #for i in range(len(move)-1,0,-1):
        #    tmp.append((move[i]+1)%4)
        move.extend(tmp)
    
    for i in move:
        nx = x+dir[i][0]
        ny = y+dir[i][1]
        
        #런타임에러
        #if 0<=nx<=100 and 0<=ny<=100:
            
        a[nx][ny] = 1
        x = nx
        y = ny 

count = 0

for i in range(100):
    for j in range(100):
        if a[i][j] == 1:
            if a[i+1][j] == 1 and a[i][j+1] == 1 and a[i+1][j+1] == 1:
                count += 1

print(count)