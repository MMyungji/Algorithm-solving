def solution(priorities, location):
    answer = 0 
    p = [(v,i) for i,v in enumerate(priorities)]
    m = max(priorities)
    #print("max: ", m)

    while True:
        #print(p)
        pi = p.pop(0)
        #print(pi)
        #print(pi[0])

        #최대값과 같으면 프린트 출력!
        if m == pi[0]:
            #출력하므로 answer번째 출력 +1
            answer += 1
            #출력한 값 제외, 다시 max값 구하기
            priorities.pop(0)
            m = max(priorities)

            #최대값의 인덱스가 내가 요청한 인덱스값과 같음 break!
            if location == pi[1]:
                break

        #최대값보다 작으면 
        else:
            #pop()한 것 맨 마지막에 배치
            p.append(pi)
            priorities.append(priorities.pop(0))

    return answer




p1 = [2, 1, 3, 2]
l1 = 2
print(solution(p1, l1))


p2 = [1, 1, 9, 1, 1, 1]
l2 = 0
print(solution(p2, l2))
