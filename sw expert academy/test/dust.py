#미해결 문제

import sys
dx = [-1,0,1,0]
dy = [0,-1,0,1]

def spread(x,y):
    count = dust[x][y]
    for d in range(4):
        nx = x+dx[d]
        ny = y+dy[d]

        if 0<=nx<=R and 0<=ny<=C:
            dust[nx][ny] += count//5
            dust[x][y] -= count//5

#def clean():
    


    


R, C, T = map(int,input().split())
dust = [list(map(int,input().split)) for _ in range(R)]

