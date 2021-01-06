'''
백준 11726번 2xN 타일링 2
    : D[n] = D[n-1] + 2*D[n-2]
'''

n = int(input())

#비 재귀 코드 > 성공
d = [0,1,3]

for i in range(3,n+1):
    d.append(d[i-1]+2*d[i-2])

print(d[n]%10007)


#재귀 코드 > 런타인에러
s = [0] * 1000

def solve(x):
    if x == 1: return 1
    if x == 2: return 3
    if s[x]: return s[x]
    s[x] = (solve(x-1)+2*solve(x-2))%10007
    return s[x]

print(solve(n))