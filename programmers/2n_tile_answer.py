'''
프로그래머스 동적 프로그래밍
2 x n 타일링
피보나치수열
'''
def solution(n):
    v1, v2 = 1,1
    for _ in range(n):
        v1,v2 = v2, v1+v2

    return v1%1000000007

print(solution(5))