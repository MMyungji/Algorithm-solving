#깊이/너비 우선 탐색(DFS/BFS) 단어 변환
def solution(begin, target, words):
    answer = 0

    # 
    visited = [0 for i in words]
    stack = [begin]

    if target not in words:
        return 0

    
    while stack:
        v = stack.pop()
        #print('v: ',v)
        if v == target:
            return answer

        for i in range(len(words)):
            print("#{} {} = {}".format(words[i], v, [1 for j in range(len(words[i])) if words[i][j] != v[j]]))
            if len([j for j in range(len(words[i])) if words[i][j] != v[j]]) == 1:
                if visited[i] != 0:
                    continue
                visited[i] = 1
                stack.append(words[i])
                #print(stack)
            
        answer+=1




b = "hit"
t = "cog"
w = ["hot", "dot", "dog", "lot", "log", "cog"]
print(solution(b,t,w))