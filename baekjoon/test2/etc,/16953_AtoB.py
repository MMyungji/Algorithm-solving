'''
백준 16953번 A->B

우선순위 큐
'''
import heapq

A,B = map(int, input().split())

visited = []
q = []

heapq.heappush(q, [1,A])
answer = -1

while q:
    level,n = heapq.heappop(q)
    visited.append(n)

    if n == B:
        answer = level
        break
    else:
        ni = n*2
        nj = n*10 + 1

        if ni not in visited and ni not in q and ni <= B:
            heapq.heappush(q, [level+1, ni])
        if nj not in visited and nj not in q and nj <= B:
            heapq.heappush(q, [level+1,nj])

print(answer)

