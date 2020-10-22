'''
백준 10451번 순열 사이클
bfs사용
'''
from collections import deque

def bfs(n):
    q = deque()
    q.append([n,arr[n-1]])

    while q:
        s,e = q.popleft()
        visited[s] = 1

        if visited[e] == 0:
            q.append([e,arr[e-1]])
        else:
            break


testcase = int(input())
for _ in range(testcase):
    n = int(input())
    arr = list(map(int,input().split()))

    visited = [0]*(n+1)
    count = 0
    for i in range(1,n+1):
        if visited[i] == 0:
            bfs(i)
            count += 1

    print(count)



   

    
        

    
