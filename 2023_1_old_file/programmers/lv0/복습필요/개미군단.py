def solution(hp):
    # 장군개미 5
    # 병정개미 3
    # 일개미 1
    # 최소한의 병력
    
    
    power = hp
    count = 0
    while True:
        if power - 5 >= 0:
            power -= 5
            count += 1
        else:
            break
    while True:
        if power -3 >= 0:
            power -= 3
            count += 1
        else:
            break
    while True:
        if power -1 >= 0:
            power -= 1
            count += 1
        else:
            
            break
    
    return count


# 조금 헷갈련던 문제 그래도 풀었다.
