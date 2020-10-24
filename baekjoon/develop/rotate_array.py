'''
백준 16935 배열돌리기3
arr[::-1] : 배열 역순
list(zip(*arr)) : 행열 치환
'''

'''
#배열 상하 반전
def reverse_up_down():
    global arr
    arr = arr[::-1]

#배열 좌우 반전
def reverse_left_right():
    global arr
    for i in range(N):
        arr[i] = arr[i][::-1]

#배열 오른쪽으로 90도 회전
def rotate_right():
    global arr, N, M
    temp = M
    M = N
    N = temp
    arr = [list(row)[::-1] for row in list(zip(*arr))]

#배열 왼쪽으로 90도 회전
def rotate_left():
    global arr, N, M
    temp = M
    M = N
    N = temp
    arr = [list(row) for row in list(zip(*arr))[::-1]]

#구역 나눠서 회전시키기
def arr_split1():
    global arr, N, M
    arr1, arr2, arr3, arr4 = [], [], [], []

    for i in range(N/2):
        for j in range(M/2):
            arr1[i][j] = arr[i][j]
            arr2[i][j] = arr[i][M/2+j]
            arr3[i][j] = arr[N/2+i][M/2+j]
            arr4[i][j] = arr[N/2+i][j]

    for i in range(N):
        if i<N/2:
            arr[i] = arr4[i]+arr1[i]
        else:
            arr[i] = arr3[i]+arr2[i]

'''    
    
N,M,R = map(int,input().split())

arr = [input().split() for _ in range(N)]

test = list(map(int,input().split()))

def solve(num):
    global arr
    global N
    global M

    if num == 1:
        arr = arr[::-1]

    elif num == 2:
        for i in range(N):
            arr[i] = arr[i][::-1]
    
    elif num == 3:
        temp = M
        M = N
        N = temp
        arr = [list(row)[::-1] for row in list(zip(*arr))]

    elif num == 4:
        temp = M
        M = N
        N = temp
        arr = [list(row) for row in list(zip(*arr))[::-1]]

    elif num == 5 or num == 6:
        int_N = int(N/2)
        int_M = int(M/2)

        arr1, arr2, arr3, arr4 = [[0]*int_M for _ in range(int_N)], [[0]*int_M for _ in range(int_N)], [[0]*int_M for _ in range(int_N)], [[0]*int_M for _ in range(int_N)]

        #print(int_N, int_M)
        for i in range(int_N):
            for j in range(int_M):
                arr1[i][j] = arr[i][j]
                arr2[i][j] = arr[i][int_M+j]
                arr3[i][j] = arr[int_N+i][int_M+j]
                arr4[i][j] = arr[int_N+i][j]
        
        if num == 5:
            for i in range(int_N):
                    #print(arr4[i]+arr1[i])
                    arr[i] = arr4[i]+arr1[i]
                    arr[int_N+i] = arr3[i]+arr2[i]
        else:
            for i in range(int_N):
                    arr[i] = arr2[i]+arr3[i]
                    arr[int_N+i] = arr1[i]+arr4[i]

    else:
        print("Invaild Input")




for i in test:
    solve(i)

for i in range(N):
    for j in range(M):
        print(arr[i][j], end=" ")
    print()

