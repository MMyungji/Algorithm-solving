'''
프로그래머스 여행경로
DFS, stack
'''

def solution(tickets):
    tickets.sort(reverse = True)
    
    t = {}
    for s,e in tickets:
        if s not in t:
            t[s] = [e]
        else:
            t[s].append(e) 
    #print(t)

    stack = ["ICN"]
    visited = []

    while stack:
        departure = stack[-1]
        if departure not in t or len(t[departure])==0:
            #print(stack)
            #print(t)
            visited.append(stack.pop())
        else:
            #print(t[departure])
            stack.append(t[departure].pop())
    visited.reverse()
    return visited

tickets = [["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]]
print(solution(tickets))