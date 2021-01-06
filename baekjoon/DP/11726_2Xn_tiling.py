'''
백준 11726번 2xN 타일링
    : D[n] = D[n-1] + D[n-2]
'''

n = int(input())

#재귀코드
d = [0]*1000

def solve(n):
    if n == 1: return 1
    if n == 2: return 2
    if d[n]: return d[n]
    d[n] = (solve(n-1)+solve(n-2))%10007
    return d[n]

print(solve(n))


#비 재귀 코드
s = [0,1,2]

for i in range(3,n+1):
    s.append(s[i-1] + s[i-2])

print(s[n] % 10007)