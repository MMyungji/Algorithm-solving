def solution(n, computers):
    answer = 0

    #컴퓨터 개수 만큼
    visited = [0 for _ in range(n)]

    def dfs(start):
        print("dfs START")
        #stack 이용
        st = [start]
        
        #stack이 비어있으면 네트워크 하나 형성된 것
        while st:
            print(f"st : {st}")
            #현재 컴퓨터 번호
            com_num=st.pop()
            print(f"com_num : {com_num}")

            #방문 체크
            if visited[com_num] == 0:
                visited[com_num] = 1
                print(f"visited {visited}")
            #행 개수 만큼(컴퓨터 개수) 반복문 > 연결되어있고 방문하지 않은 곳을 stack에 추가
            #연결된 노드끼리가 하나이기 때문에 연결된 노드 체크
            for i in range(len(computers[0])):
                print(f"com_num, i = {computers[com_num][i]}, visited[i] = {visited[i]}")
                if computers[com_num][i] == 1 and visited[i]==0:
                    print("i'm in")
                    st.append(i)
                    
    
    #첫번째 컴퓨터부터 체크
    idx=0
    #방문 체크
    while 0 in visited:
        #방문하지 않은 경우
        if visited[idx]==0:
            dfs(idx)
            #dfs 끝나면 네트워크 하나 찾음
            answer+=1
        #다음 컴퓨터로
        idx+=1
                    
    return answer

num = int(input())
com = [[1, 1, 0], [1, 1, 0], [0, 0, 1]]




