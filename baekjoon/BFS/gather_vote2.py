'''
백준 17779 게더맨더링 2

구현문제
중복 순열 > itertools product(list, repeat = N)
최소구할때, math.inf사용
'''
from itertools import product as pd
import math


#인구 수 구해서, (최대)-(최소) 계산, 그 중 최소값 반환
def solve(x,y,d1,d2):
    new_area = [[0]*(N+1) for _ in range(N+1)]

    #구역별 사람 수 저장, 리스트
    people = [0]*5

    #5구역
    for i in range(d1+1):
        new_area[x+i][y-i] = 5
        new_area[x+d2+i][y+d2-i] = 5
        
    for j in range(d2+1):
        new_area[x+j][y+j] = 5
        new_area[x+d1+j][y-d1+j] = 5
    
    #1구역
    for r in range(1,x+d1):
        for c in range(1,y+1):
            if new_area[r][c] == 5:
                break
            else:
                people[0] += area[r-1][c-1]
    
    #2구역
    for r in range(1,x+d2+1):
        for c in range(N,y,-1):
            if new_area[r][c] == 5:
                break
            else:
                people[1] += area[r-1][c-1]
    
    #3구역
    for r in range(x+d1,N+1):
        for c in range(1,y-d1+d2):
            if new_area[r][c] == 5:
                break
            else:
                people[2] += area[r-1][c-1]

    #4구역
    for r in range(x+d2+1,N+1):
        for c in range(N,y-d1+d2-1,-1):
            if new_area[r][c] == 5:
                break
            else:
                people[3] += area[r-1][c-1]

    #구역 5를 따로 계산하면 중복계산 할 수 있기 때문에
    #(전체 - 나머지) 로 구하기
    people[4] = total-sum(people)

    return max(people) - min(people)



N = int(input())
area = [list(map(int,input().split())) for _ in range(N)]

total = 0
for i in area:
    total += sum(i)

#중복가능한 순열사용 > 케이스 만들기
all_case = list(pd(range(1,N+1), repeat=4))
case = []
for x,y,d1,d2 in all_case:
    #if 1<= x+d1+d2 <= N and 1<= y-d1+d2 <=N : #범위 오류가 생김
    # 각 따로 해주는 것이 좋음
    if x+d1+d2 > N:
        continue
    if y-d1 < 1:
        continue
    if y+d2 > N:
        continue    

    case.append([x,y,d1,d2])


answer = math.inf
for x,y,d1,d2 in case:
    answer = min(answer,solve(x,y,d1,d2))

print(answer)


'''
#itertools 사용안하고 하는 방법
answer = math.inf
for x in range(1,N+1):
    for y in range(1,N+1):
        for d1 in range(1,N+1):
            for d2 in range(1,N+1):
                if x+d1+d2 > N:
                    continue
                if y-d1 < 1:
                    continue
                if y+d2 > N:
                    continue    

                answer = min(answer,solve(x,y,d1,d2))

print(answer)

'''



