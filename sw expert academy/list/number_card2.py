import sys

#sys.stdin = open("input.txt", "r")

T = int(input())

for test_case in range(1, T + 1):
    num = int(input())
    num_list = list(map(int, list(input())))

    num_check = [0]*10

    for n in num_list:
        num_check[n] += 1

    max_count = max_num = -1

    for i in range(9, -1, -1):
        if  num_check[i] > max_count:
            max_count = num_check[i]
            max_num = i

    print('#{} {} {}'.format(test_case, max_num, max_count)) 

