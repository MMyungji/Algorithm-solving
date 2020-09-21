#import sys
#sys.stdin = open("input.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    arr = input()
    test_arr = list(map(int,arr.split()))
    print("test_arr: ", test_arr)
    stations_array = input()
    stations = list(map(int,stations_array.split()))
    print("stations: ", stations)
    now = 0
    past = -1
    count = 0
    while now < test_arr[1]:
        if now == 0 or now in stations:
            
            if now == past:
                count = 0
                break
            else:
                past = now
                if now+test_arr[0] >= test_arr[1]:
                    break
                else:
                    now+=test_arr[0]
                    count += 1
        else:
            now -=  1
            print("count DOWN")
    print("#{} {}".format(test_case, count))
            
        