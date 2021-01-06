'''
백준 14395 4연산
 : 정수 s의 값을 t로 바꾸는 최소 연산 횟수

1. 최소 연산 횟수 구하기
    : bfs, 큐사용
2. set() - 집합을 이용한 숫자 방문여부 확인
'''
from collections import deque

s,t = map(int,input().split())

#bfs, (현재 숫자, 현재까지의 연산)
q = deque()
q.append([s,''])

#set()을 이용해 방문 여부 확인
check = set()
check.add(s)

if s == t:
    print(0)
else:
    res = -1
    while q:
        c_v,c_s = q.popleft()
        if c_v == t:
            res = c_s
            print(res)
            exit(0)

        #연산의 우선순위대로 q에 추가
        n_v = c_v*c_v
        if 0<=n_v<=t and n_v not in check:
            q.append([n_v, c_s+'*'])
            check.add(n_v)
        
        n_v = c_v+c_v
        if 0<=n_v<=t and n_v not in check:
            q.append([n_v, c_s+'+'])
            check.add(n_v)
        
        #나누기를 한 경우(자기자신을 나누는 것임으로 1)
        n_v = 1
        if n_v not in check:
            q.append([n_v, c_s+'/'])
            check.add(n_v)

        #뺄셈은 0이 되므로 더이상 연산을 진행할 수 없다. > 뺄셈은 제외
        

    print(res)
