'''
백준 17140 이차원 배열과 연산

1. 행열 바꾸기 > list(zip(*arr))
2. 딕셔너리 정렬 > 리스트로 바뀐다 [( ),( ),( )...]
sorted(calc_num.items(),key=lambda x: (x[1],x[0]))
: x[1]은 values, x[0]은 keys
'''
from collections import Counter
R,C,K = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(3)]
answer = 0

while answer <= 100:
    if R <= len(arr) and C <= len(arr[0]) and arr[R-1][C-1] == K:  #A[r][c] = k
        break

    r_cnt = len(arr)
    c_cnt = len(arr[0])

    #시간 
    answer += 1
    C_flag = False
    if r_cnt < c_cnt:
        C_flag = True
        arr = list(zip(*arr))
    
    max_len = 0
    for i in range(len(arr)):
        calc_num = Counter(arr[i])
        if calc_num[0]:
            del calc_num[0]
        sorted_calc_num = sorted(calc_num.items(),key=lambda x: (x[1],x[0]))
        
        calc_arr = []
        for num,cnt in sorted_calc_num:
            calc_arr.extend((num,cnt))
        arr[i] = calc_arr
        max_len = max(max_len, len(calc_arr))
    
    for j in range(len(arr)):
        if len(arr[j])<max_len:
            for _ in range(max_len-len(arr[j])):
                arr[j].append(0)

    if C_flag == True:
        arr = list(zip(*arr))

if answer > 100:
    answer = -1
         
print(answer)
