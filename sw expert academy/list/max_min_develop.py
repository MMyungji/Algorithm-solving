T = int(input())

for test_case in range(1, T + 1):
    N, M= list(map(int,input().split()))

    num_list = list(map(int,input().split()))

    sum_num = []
    count = 0
    
    for i in range(M,N+1):
        temp = sum(num_list[:i]) - sum(num_list[:count])
        #print("{}-{}={}".format(i,i-count,temp))
        sum_num.append(temp)
        count += 1

    result = max(sum_num) - min(sum_num)
    #print("result: ", result)
    print("#{} {}".format(test_case, result))
    

