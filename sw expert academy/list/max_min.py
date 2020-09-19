def max_num(num):
    result = num[0]
    for i in range(1, len(num)):
        if result < num[i]:
            result = num[i]
    return result

def min_num(num):
    result = num[0]
    for i in range(1, len(num)):
        if result > num[i]:
            result = num[i]
    return result

T = int(input())

for test_case in range(1, T + 1):
    nums = input()
    n = list(map(int,input().split()))
    print("#{} {}".format(test_case, max_num(n)-min_num(n)))
    