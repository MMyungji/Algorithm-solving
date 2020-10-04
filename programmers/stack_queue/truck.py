def solution(bridge_length, weight, truck_weights):
    answer = 0
    ing = [0] * bridge_length
    while ing:
        answer += 1
        ing.pop(0)
        print("#ing {}".format(ing))
        print("#trucks {}".format(truck_weights))
        if truck_weights:
            if sum(ing) + truck_weights[0] <= weight:
                ing.append(truck_weights.pop(0))
            else:
                ing.append(0)
            print("##ing {}".format(ing))

    return answer



b = 2

w = 10

t = [7,4,5,6]

print(solution(b,w,t))