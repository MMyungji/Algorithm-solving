def solution(cookies,k):
    answer = []
    q = []
    for i in range(len(cookies)):
        q.append([cookies[i],i])
        
    while q:

        n,l = q.pop(0)
        
        snacks = []
        
        for i in range(l,len(cookies)):
            snack = [n]
            if cookies[i] > n:
                snack.append(cookies[i])
                for j in range(i,len(cookies)):
                    if cookies[j] > cookies[i]:
                        snacks.append(snack + [cookies[j]])
                    else:
                        snacks.append(snack)
            else:
                snacks.append(snack)
        answer.extend(snacks)
    
    result = []
    max_len = max([len(i) for i in answer])
    for a in answer:
        if len(a) == max_len and a not in result:
            result.append(a)
    
    #result.sort()
    print(result)
    return result[k-1]

print(solution([1,4,2,6,5,3],2))
print(solution([4,2,6,5,3],2))
print(solution([6,5,3],1))