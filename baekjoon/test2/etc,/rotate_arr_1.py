'''
SW 역량 테스트 준비 - 문제 2

16926번 배열돌리기 1
시뮬레이션
시간초과: deepcopy때문인가? 아님 for문 때문인가?
'''
from copy import deepcopy as dc
N, M, R = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

def rotate(i,n,m):
    global arr 
    r_arr = dc(arr)

    #행
    for x in range(n): 
        r_arr[i+x+1][i] = arr[i+x][i]
        r_arr[i+n-x-1][i+m] = arr[i+n-x][i+m]
    #열
    for y in range(m): 
        r_arr[i+n][i+y+1] = arr[i+n][i+y]
        r_arr[i][i+m-y-1] = arr[i][i+m-y]

    arr = r_arr
    '''
    print(f"<< {i}, {i} 돌리기 >>")
    for q in range(len(arr)):
        print(arr[q])
    '''

#행,열 중 최소
min_nm = min(N,M)

for _ in range(R):
    #회전 시, 움직이는 행열수 변화 
    n_num = N-1
    m_num = M-1 

    for i in range(min_nm//2):
        rotate(i,n_num,m_num)
        n_num-=2
        m_num-=2

#출력
for ar in arr:
    for a in ar:
        print(a, end=" ")
    print()