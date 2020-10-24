'''
백준 17140 이차원 배열과 연산 

런타임에러
'''
R,C,K = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(3)]
answer = 0


def r_calc():
    global arr,r_cnt,c_cnt
    new_arr = [[] for _ in range(r_cnt)]
    for i in range(r_cnt):
        count_num = {}
        for num in arr[i]:
            if num == 0:
                continue
            if num in count_num:
                count_num[num] += 1
            else:
                count_num[num] = 1

        temp = []
        #정렬하기
        sorted_cnt = sorted(count_num.items(), key=lambda x: (x[1],x[0]))
        #print(sorted_cnt)

        for k,v in sorted_cnt:
            temp.append(k)
            temp.append(v)
        new_arr[i] = temp
        if c_cnt<len(new_arr[i]):
            c_cnt = len(new_arr[i])
    arr = new_arr
    #print(arr)
    #print(c_cnt)
    for n in range(r_cnt):
        for m in range(c_cnt):
            if m >= len(arr[n]):
                arr[n].append(0)
    #print("R연산")
    #print(arr)

def c_calc():
    global arr, c_cnt, r_cnt

    arr = list(zip(*arr))
    new_arr = [[] for _ in range(c_cnt)]
    for i in range(c_cnt):
        count_num = {}
        for num in arr[i]:
            if num == 0:
                continue
            if num in count_num:
                count_num[num] += 1
            else:
                count_num[num] = 1

        temp = []
        #정렬하기
        sorted_cnt = sorted(count_num.items(), key=lambda x: (x[1],x[0]))
        #print(sorted_cnt)

        for k,v in sorted_cnt:
            temp.append(k)
            temp.append(v)
        new_arr[i] = temp
        if r_cnt<len(new_arr[i]):
            r_cnt = len(new_arr[i])
    arr = new_arr
    #print(arr)
    #print(c_cnt)
    for n in range(c_cnt):
        for m in range(r_cnt):
            if m >= len(arr[n]):
                arr[n].append(0)

    arr = list(zip(*arr))
    #print("C연산")
    #print(arr)





while answer <= 100:
    if arr[R-1][C-1] == K:  #A[r][c] = k
        break

    r_cnt, c_cnt = 0, 0
    for _ in arr:
        r_cnt += 1
    for _ in arr[0]:
        c_cnt += 1

    #시간 
    answer += 1
    if r_cnt >= c_cnt:
        r_calc()
    else:
        
        c_calc()
         
print(answer)
