'''
백준 17779 게더맨더링 2

1. 추론
구현문제
중복 순열 > itertools product(list, repeat = N)
큐 > deque

시간초과 ㅠㅠ
'''

from collections import deque
from itertools import chain as ch
from itertools import product as pd

d = [(0,1),(0,-1),(1,0),(-1,0)]


#구역별 인구수 구하기
def bfs(r,c):
    q = deque()
    num = new_area[r][c]
    #print(f"{num} 인구수 세기 시작")

    q.append([r,c])

    #해당 구역 총 인구 수
    total = 0
    while q:
        i,j = q.popleft()
        visited[i][j] = True
        total+=area[i][j]
        #print(f"total 인구수 = {total}")

        for di,dj in d:
            nx = i+di
            ny = j+dj

            if not (0<=nx<N and 0<=ny<N):
                continue
            if visited[nx][ny] == False and [nx,ny] not in q and new_area[nx][ny] == num:
                q.append([nx,ny])
    return total



N = int(input())
area = [list(map(int,input().split())) for i in range(N)]

all_list = list(pd(range(1,N), repeat=4))

#조건에 맞는 경우의 수
test = []
for x,y,d1,d2 in all_list:
    if 1<=x+d1<=N and 1<=y-d1<=N and 1<=(x+d1+d2)<=N and 1<=(y+d2-d1)<=N and 1<=x+d2<=N and 1<=y+d2<=N:
        if 1<=x<=N-1 and 2<=y<=N:
            test.append([x-1,y-1,d1,d2])

#가장 많은 인구수 - 가장 적은 인구수 : 결과 저장 리스트
gap_pop = []

#구획 나누기
for x,y,d1,d2 in test:
    new_area = [[0]*N for _ in range(N)]

    #print(f"x: {x}, y: {y}, d1: {d1}, d2: {d2}")

    #5 경계 세우기
    for i in range(d1+1):
        #if (0<=x+i<N and 0<=y-i<N and 0<=(x+i+d2)<N and 0<=(y+d2-i)<N):
        new_area[x+i][y-i]=5
        new_area[x+d2+i][y+d2-i]=5
    for i in range(d2+1):
        #if (0<=x+i<N and 0<=y+i<N and 0<=(x+d1+i)<N and 0<=(y+i+d1)<N):
        new_area[x+i][y+i] = 5
        new_area[x+d1+i][y-d1+i] = 5

    #5 경계 안 채우기
    for i in range(d1):
        k=1
        while new_area[x+i+k][y-i] != 5:
            new_area[x+i+k][y-i] = 5
            k+=1
    for i in range(d2):
        k=1
        while new_area[x+i+k][y+i] != 5:
            new_area[x+i+k][y+i] = 5
            k+=1

    '''
    # 새로운 선거구역 완성
    for r in range(N):
        for c in range(N):
            if (0<=r<(x+d1) and 0<=c<=y):
                if new_area[r][c] == 5:
                    continue
                new_area[r][c] = 1
                continue
            if 0<=r<=(x+d2) and y<c<N:
                if new_area[r][c] == 5:
                    continue
                new_area[r][c] = 2
                continue
            if x+d1<=r<N and 0<=c<y-d1+d2:
                if new_area[r][c] == 5:
                    continue
                new_area[r][c] = 3
                continue
            if x+d2<=r<N and y-d1+d2<=c<N:
                if new_area[r][c] == 5:
                    continue
                new_area[r][c] = 4
                continue
    '''
    for r in range(N):
        for c in range(N):
            if new_area[r][c] != 5:
                if (0<=r<(x+d1) and 0<=c<=y):
                    new_area[r][c] = 1
                    continue
                if 0<=r<=(x+d2) and y<c<N:
                    new_area[r][c] = 2
                    continue
                if x+d1<=r<N and 0<=c<y-d1+d2:
                    new_area[r][c] = 3
                    continue
                if x+d2<=r<N and y-d1+d2<=c<N:
                    new_area[r][c] = 4
                    continue


    
    #if list(set(ch(*new_area))) != [1,2,3,4,5]:
    #    continue

    
    #print("구획 나눔")
    #for new_row in new_area:
    #    print(new_row)

    #print("")

    # 인구수 저장
    population = []
    # 방문 여부 확인
    visited = [[False]*N for _ in range(N)]

    for i in range(N):
        for j in range(N):
            if visited[i][j] == False:
                pop_num = bfs(i,j)
                #print(f"[{new_area[i][j]}] : {pop_num}")
                population.append(pop_num)

    # (가장 많은 인구수 - 가장 적은 인구수) 저장
    #print(f"{max(population)} - {min(population)} =  {(max(population) - min(population))}")
    gap_pop.append(max(population) - min(population))
    #print("gap_pop: ",gap_pop)

#(가장 많은 인구수 - 가장 적은 인구수)의 최솟값
print(min(gap_pop))

