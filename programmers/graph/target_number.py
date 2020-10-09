def solution(numbers, target):
    answer = 0

    #모든 경우의 수를 저장하는 리스트
    sup = [0]

    #더하고 빼는 계산
    for i in numbers:
        #이전의 결과값을 저장하는 리스트
        sub = []
        #이전의 결과 값에 현재의 수 더하고 빼기
        for j in sup:
            sub.append(j+i)
            sub.append(j-i)
        #결과 저장
        sup = sub

    answer = sup.count(target)

    return answer