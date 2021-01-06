'''
백준 12871번 무한문자열

'''
import math

def solve(arr1,arr2):
    len1 = len(arr1)
    len2 = len(arr2)

    #두 수의 최소공배수 구하기
    len3 = len1*len2 // math.gcd(len1, len2)

    a = ''
    b = ''

    #최소공배수만큼 문자열 늘리기
    for _ in range(len3//len1):
        a+=arr1
    for _ in range(len3//len2):
        b+=arr2    

    #늘린 문자열 비교
    if a == b:
        return 1
    else:
        return 0

arr1 = input()
arr2 = input()

print(solve(arr1,arr2))
