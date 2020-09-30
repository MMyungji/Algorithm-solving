T = int(input())
for test_case in range(1, T + 1):
    case = int(input())

    #집합 set: 중복X 순서X
    color = [set({}), set({})]


    for i in range(case):
        #띄어쓰기로 변수 나누어서 저장
        x1,y1,x2,y2,c = map(int, input().split())

        #print("{} {} {} {} {}".format(x1,y1,x2,y2,c))

        #원소생성
        for x in range(x1, x2+1):
            for y in range(y1, y2+1):
                color[c-1].add((x,y))
        
    #print(color)

    #교집합 & 사용
    result = color[0] & color[1]

    #print(result)

    print("#{} {}".format(test_case, len(result)))

