def solution(N, stages):
    dict_ = {}
    cnt = len(stages)
    
    for i in range(1, N+1):
        if cnt != 0:
            dict_[i] = (stages.count(i)/cnt)
            cnt -= stages.count(i)
        else:
            dict_[i] = 0
    return sorted(dict_, key=lambda x: dict_[x], reverse = True)        

    
