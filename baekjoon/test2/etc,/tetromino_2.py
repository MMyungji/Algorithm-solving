'''
SW 역량 테스트 준비 - 문제 1

<<제출버전 - Pypy로 제출>>
백준 14500번 테트로미노
브루트포스
'''

N,M = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(N)]
tetromino = [
    [(0,0),(0,1),(1,0),(1,1)],
    [(0,0),(0,1),(0,2),(0,3)], [(0,0),(1,0),(2,0),(3,0)],
    [(0,0),(0,-1),(-1,-1),(-2,-1)],[(0,0),(0,1),(-1,1),(-2,1)],\
    [(0,0),(1,0),(1,1),(1,2)],[(0,0),(1,0),(1,-1),(1,-2)],\
    [(0,0),(-1,0),(-1,1),(-1,2)],[(0,0),(-1,0),(-1,-1),(-1,-2)],\
    [(0,0),(0,-1),(1,-1),(2,-1)],[(0,0),(0,1),(1,1),(2,1)],
    [(0,0),(0,1),(0,2),(1,1)],\
    [(0,0),(0,1),(0,2),(-1,1)],\
    [(0,0),(0,1),(-1,1),(1,1)],\
    [(0,0),(-1,-1),(0,-1),(1,-1)],
    [(0,0),(1,0),(1,1),(2,1)],\
    [(0,0),(1,0),(1,-1),(2,-1)],\
    [(0,0),(0,-1),(1,-1),(1,-2)],\
    [(0,0),(0,1),(1,1),(1,2)]
]

result = 0
for i in range(N):
    for j in range(M):
        for ti in range(19):
            value = 0
            for tj in range(4):
                ni = i+tetromino[ti][tj][0]
                nj = j+tetromino[ti][tj][1]
                try:
                    value += arr[ni][nj]
                except:
                    break
            result = max(value,result)

print(result)
