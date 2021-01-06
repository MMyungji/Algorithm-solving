'''
백준 11779번 최소비용 구하기2

1. 다익스트라, 최소경로
2. 최단 거리 찾으면, 최솟값을 넣고 path갱신

'''
import heapq 

n = int(input())
m = int(input())
route=[[] for _ in range(n+1)]
 
#최대값 저장
INF=1e9
 
for _ in range(m):
    s,e,cost=map(int,input().split())
    route[s].append([e, cost])

S,E=map(int,input().split())#출발,도착

distance = [INF for _ in range(n+1)] # 거리 
path = [[] for _ in range(n+1)] # 경로를 담을 배열 
path[S].append(S)

q=[]
heapq.heappush(q,[0,S])

while q:
    now_cost, now = heapq.heappop(q)
 
 #현재경로가 이전 경로보다 길다면 연결된 노드에대해 탐색할 필요없음
    if now_cost > distance[now]:
        continue
 
    if now == S:
        distance[now] = 0

    #다음 경로     
    for next_city, next_cost in route[now]:
        costs = next_cost + now_cost
        if costs < distance[next_city]:
            distance[next_city] = costs
            heapq.heappush(q, (costs, next_city))
            
            # path 가 갱신됐을 때 현재까지의 경로를 넣어준다. 
            path[next_city] = []
            for p in path[now]:
                path[next_city].append(p)
            path[next_city].append(next_city)

print(distance[E]) 
print(len(path[E])) 
print(' '.join(map(str,path[E])))