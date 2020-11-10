'''
프로그래머스 동적 프로그래밍
2 x n 타일링
조합이용
'''

from itertools import permutations as p

def solution(n):
    answer = 0
    for i in range(n%2,n+1,2):
        temp = [1]*i + [2]*((n-i)//2)
            
        answer += len(list(set(list(p(temp,len(temp))))))

    return answer

print(solution(5))