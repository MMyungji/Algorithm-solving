'''
백준 15686 치킨배달
구현 이용 - 브루트 포스

itertools.combinations(범위, 조합수) : 조합
abs(num) : 절댓값 구하기
'''
import sys
import itertools 

N , M = map(int, sys.stdin.readline().split())
city = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

home = []
chicken = []

#집, 치킨집 위치 구하기
for i in range(N):
    for j in range(N):
        if city[i][j] == 1:
            home.append([i+1,j+1])
        elif city[i][j] == 2:
            chicken.append([i+1,j+1])
        else:
            continue

#남은 치킨 집 조합
new = list(itertools.combinations(chicken,M))

#도시의 치킨 거리 구한 리스트
sum_chicken = []

#도시의 치킨거리 최솟값 구하기
while new:
    new_chicken = new.pop()

    #치킨집이었던 곳 찾아 0으로 변환
    for chicken_idx in chicken:
        if chicken_idx not in new_chicken:
            city[chicken_idx[0]-1][chicken_idx[1]-1] = 0

    #집과 치킨집으로의 도시 치킨 거리 구해 리스트에 넣기
    dist = 0
    for i,j in home:
        #집마다 최소거리 구해 더하기
        temp = []
        for x,y in new_chicken:
            temp.append((abs(i-x) + abs(j-y)))
        dist += min(temp)
        
    sum_chicken.append(dist)

print(min(sum_chicken))
