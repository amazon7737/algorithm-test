
# count 를 구현하지 못함. 트럭 옮기는 과정은 완성함

from collections import deque
def solution(bridge_length, weight, truck_weights):
    # 다리에 올라갈 수 있는 트럭 수 : bridge_length
    # 다리가 견딜 수 있는 무게 : weight
    # 트럭 별 무게 : truck_weights
    
    # trucked : 다리를 지난 트럭 배열
    # trucking : 다리를 건너는 트럭 배열
    trucked=deque()
    trucking=deque()
    truck_weights = deque(truck_weights)
    cnt=1
    bridge = [0 for _ in range(bridge_length)]

    while len(truck_weights) != 0:
        
        cnt+=1    
        if (sum(trucking) + truck_weights[0]) <= weight:
            # trucking 
            trucking.append(truck_weights.popleft())
        else:    
            trucked.append(trucking.popleft())
        print("-----")    
        print("truck_weights:",truck_weights)
        print("trucking:",trucking)
        print("trucked:",trucked)
    print("cnt:",cnt)    


# 해설

from collections import deque


def solution(bridge_length, weight, truck_weights):
    answer = 0
    d = deque([0] * bridge_length)
    truck_weights = deque(truck_weights)
    total_weight = 0

    while d:
        total_weight -= d.popleft()

        if truck_weights:
            if total_weight + truck_weights[0] <= weight:
                w = truck_weights.popleft()
                d.append(w)
                total_weight += w
            else:
                d.append(0)
        answer += 1

    return answer
