'''
백준 1697 숨바꼭질
dfs, 재귀사용 > 무한 루프
bfs,deque 사용!
'''
from collections import deque

N, K = map(int,input().split())

#큐는 방문 위치 체크 필수
visited = [False] * 100001

def bfs(s):
    count = 0
    q = deque()
    #시작 위치와 카운트 수
    q.append([s, count])

    while q:
        now_location = q.popleft()
        now = now_location[0]    #현재 위치
        count = now_location[1]      #현재까지의 카운트 수

        #현재 위치 방문 전이라면! 
        #방문 한 곳이면 다시 방문 할 필요 없음 > 무한 반복하기 때문
        if visited[now] == False:
            visited[now] = True

            if now == K:
                return count

            count+=1
            if (now - 1) >= 0:
                q.append([now-1,count])
            if (now + 1) <= 100000:
                q.append([now+1,count])
            if (now*2) <= 100000:
                q.append([now*2,count])

    return count

print(bfs(N))
            






