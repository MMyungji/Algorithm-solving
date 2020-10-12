T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N, K = map(int, input().split())
    turn = N//4
    numbers = list(input())
    password = []
    for _ in range(turn):
        for i in range(4):
            password.append(int("".join(numbers[i*turn:(i+1)*turn]),16))
        numbers.append(numbers.pop(0))
    password = list(set(password))
    password.sort(reverse=True)
    print(password)
    print(f"#{test_case} {password[K-1]}")