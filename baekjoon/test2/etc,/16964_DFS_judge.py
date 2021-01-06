'''
백준 16964번 DFS 스페셜 저지

1. 그래프 모양이 트리
    : 즉, 사이클이 없다
2. 양방향 그래프는 배열에 둘다 입력해준다.
3. 0또는1의 결과를 갖는 것은 flag이용하기
'''

n = int(input())
arrs = [list(map(int,input().split())) for _ in range(n-1)]
result = [0] + list(map(int,input().split()))

#방문여부
visited = [0] * (n+1)

arr = [[] for _ in range(n+1)]
for a,b in arrs:
    #양방향 그래프
    arr[a].append(b)
    arr[b].append(a)
#print("정렬 전 arr: ",arr)

flag = True
res_idx = 1

#방순 순서의 우선순위 저장
order = [0] *(n+1)
for i in range(1,n+1):
    order[result[i]] = i
#방문 우선순위대로 노드 방문 순서 정렬하기
for i in arr:
    i.sort(key=lambda x: order[x])
#print("*정렬 후 arr: ",arr)

def dfs(node):
    global flag
    global res_idx

    if not flag:
        return
    if result[res_idx] != node: #방문 순서 확인
        flag = False
        return
    res_idx += 1
    for i in arr[node]:
        if visited[i] == 0:
            visited[i] = 1
            dfs(i)

#1부터 시작
visited[1] = 1
dfs(1)

print(1 if flag else 0)