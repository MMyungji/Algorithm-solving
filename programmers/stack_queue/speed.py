import math
def solution(progresses, speeds):
    answer = []
    dev = []
    for x,y in zip(progresses, speeds):
        dev.append(math.ceil((100-x)/y))
    #ev = math.ceil((100-x)/y for x,y in zip(progresses, speeds))
    
    front = 0
    for i in range(len(dev)):
        if dev[front] < dev[i]:
            answer.append(i-front)
            front = i
    answer.append(len(dev)-front)

    return answer


prog = [93, 30, 55]
speed = [1, 30, 5]

print(solution(prog, speed))