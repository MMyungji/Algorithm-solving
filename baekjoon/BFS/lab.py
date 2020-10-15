'''
14502 연구실
BFS 재귀사용, 시간초과
'''

import sys
from collections import deque
from copy import deepcopy as dc


N, M = map(int, sys.stdin.readline().split())
lab = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
q = deque()

d = [(0,1), (0,-1), (1,0), (-1,0)]
answer = 0  #안전한 지역 개수


def bfs():
    global answer

    #깊은 복사
    new = dc(lab)

    #바이러스 찾기
    for i in range(N):
        for j in range(M):
            if new[i][j] == 2:
                q.append([i,j])

    #q = 바이러스 담는 그릇
    while q:
        i, j = q.popleft()

        for di, dj in d:
            nx = i+di
            ny = j+dj
            
            #주변에 빈칸 있으면 바이러스 퍼트리기
            #퍼진 바이러스 q에 삽입
            if 0<=nx<N and 0<=ny<M:
                if new[nx][ny] == 0:
                    new[nx][ny] = 2
                    q.append([nx,ny])
    
    #0인 개수 확인하기
    count = 0
    for list_i in new:
        count += list_i.count(0)
    
    #비교해서 더 큰 수 저장
    answer = max(answer,count)

#재귀
#모든 경우의 수 만들기 > 재귀함수 사용
#만든 모든 경우의 수를 비교
def wall(x):
    if x == 3:
        bfs()
        return
    for i in range(N):
        for j in range(M):
            if lab[i][j] == 0:
                lab[i][j] = 1
                wall(x+1)
                lab[i][j] = 0


wall(0)
print(answer) 
