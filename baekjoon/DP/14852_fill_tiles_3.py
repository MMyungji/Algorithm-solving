'''
백준 14852번 타일 채우기 3
    D[n] = 2 x D[n-1] + 3 x D[n-2] + (2 x D[n-3] + 2 x D[n-4] ... 2 x D[0]
'''

n = int(input())

#런타임 에러!
d = [0] * 1000000

def dp(x):
    if x == 0: return 1
    if x == 1: return 2
    if x == 2: return 7
    if d[x]: return d[x]

    result = 2*dp(x-1)+3*dp(x-2)

    #점화식을 따로 만들 수 있음
    for i in range(3,x+1):
        result += (2*dp(x-i)) % 1000000007
    d[x] = result % 1000000007
    return  d[x]

print(dp(n))

#2차원 dp 점화식
#런타임 에러!
'''
dd = [[0] * 2 for _ in range(1000000)]

def dp2(x):
    dd[0][0] = 0
    dd[1][0] = 2
    dd[2][0] = 7
    dd[2][1] = 1

    for i in range(3,x+1):
        d[i][1] = (d[i-1][1]+d[i-3][0]) % 1000000007
        d[i][0] = (3*d[i-2][0] + 2*d[i-1][0] + 2*d[i][1]) % 1000000007
    
    return d[x][0]

print(dp2(n))
'''
s = [1,2,7]

for i in range(3,n+1):
    result = 2*s[i-1]+3*s[i-2]
    for j in range(3,i+1):
        result += (2*s[i-j]) % 1000000007
    s.append(result % 1000000007)

print(s[n])


