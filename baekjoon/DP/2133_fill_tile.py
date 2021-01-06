'''
백준 2133번 타일 채우기 
    홀수:0
    짝수:D[n] = D[n-2] X 3 >>  틀림

    짝수개일때, 2가지 추가적으로 경우의 수가 생김
    D[n] = 3 X D[n-2] +  2 X D[n-4] + 2 X  D[n-6] ... 2 X D[0]
'''

n = int(input())
d = [0] * 31

def dp(x):
    if x == 0: return 1
    if x == 1: return 0
    if x == 2: return 3
    if d[x]: return d[x]

    result = 3*dp(x-2)
    for i in range(4,x+1,2):
        result+=2*dp(x-i)

    d[x]  = result

    return d[x]

print(dp(n))

