'''
프로그래머스 여행경로
DFS, stack, 문제 틀림
'''
def solution(tickets):
    stack = []
    stack.append("ICN")
    visited = []
    used =  []
    
    while stack:
        node = stack.pop()
        visited.append(node)
        if len(visited) > 1:
            used.append([visited[-2], visited[-1]])

        temp = []
        for ticket in tickets:
                if ticket[0] == node and ticket not in used:
                    temp.append(ticket[1])
                    
        if temp:
            temp.sort(reverse = True)
            for t in temp:
                stack.append(t)
        else:
            break
    
    return visited
            
        
        
tickets = [["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]]
print(solution(tickets))