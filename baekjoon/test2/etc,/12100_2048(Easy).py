'''
백준 12100번 2048(Easy)

브루트포스와 dfs
'''

N = int(input())
arr = [list(map(int,input().split())) for _ in range(N)]
max_value = 0

print(max_value)


def find_max(arr):
    global max_value
    for i in range(N):
        for j in range(N):
            if max_value < arr[i][j]: max_value = arr[i][j]

def move_left(board):
    for i in range(N):
        p = 0
        x = 0

        for q in range(N):
            if board[i][q] == 0: continue
            if x == 0:
                x = board[i][q]
            else:
                if x == board[i][q]:
                    board[i][p] = 2*x
                    p =+ 1
                    x = 0
                else:
                    board[i][p] = x
                    p =+ 1
                    x = board[i][q]
            board[i][q] = 0

        if x != 0: board[i][p] = x
    return board
