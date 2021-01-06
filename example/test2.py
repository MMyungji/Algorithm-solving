from itertools import product as pd
from itertools import combinations as cb
from collections import Counter
def solution(board):
    answer = 0
    
    rock = len(board)
    n = [i for i in range(rock)]
    s = list(cb(list(pd(n,repeat = 2)),rock))
    
    test=[]
    for c in s:
        x = list(set([i[0] for i in c]))
        y = list(set([j[1] for j in c]))
        if len(x) == rock and len(y) == rock:
            test.append(c)
    
    for t in test:
        temp = 0
        for x,y in t:
            temp += board[x][y]
        answer = max(answer,temp)
    return answer


b = [[3,6,8],[1,4,7],[2,1,4]]
print(solution(b))