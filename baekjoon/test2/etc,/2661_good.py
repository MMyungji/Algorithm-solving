'''
백준 2661번 좋은수열

1. 뒤에서 첫번째 숫자와 두번째 숫자는 달라야한다
2. 뒤에서 첫번째, 두번째 숫자는 세번째, 네번째 숫자와 달라야한다
'''

def isok(string):
    length = len(string)
    tempLength = range(2,length+1,2)
    #원래 문자열을 뒤집음
    string = ''.join(reversed(string))

    for temp in tempLength:
        if string[:temp//2] == string[temp//2:temp//2 * 2]:
            return False

    return True

def solve(index, ans):
    if index == N:
        print(ans)
        exit()
        return
    
    #문자 추가
    for i in ('1', '2', '3'):
        if isok(ans+i):
            solve(index+1, ans+i)


N = int(input())
solve(1, '1')