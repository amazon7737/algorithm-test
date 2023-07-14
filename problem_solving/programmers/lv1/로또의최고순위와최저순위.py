def solution(lottos, win_nums):
    # arr -> 최대로 가능한 , arr2 -> 최소로 가능한
    arr=[];arr2=[];arr3=[]
    lottos.sort();win_nums.sort()
    for i in range(len(lottos)):
        if lottos[i] in win_nums:
            arr.append(lottos[i])
            arr2.append(lottos[i])
    # 최대로 일치할경우 ,  최소로 일치할경우 ( 그냥 일치하는건만 카운트)
    # 최소로 일치할 경우        
    
    # 최대로 일치할 경우
    for _ in range(lottos.count(0)):
        arr.append(0)
# 최대로 일치
    if len(arr) == 6:
        arr3.append(1)
    elif len(arr) == 5:
        arr3.append(2)
    elif len(arr) == 4:
        arr3.append(3)
    elif len(arr) == 3:
        arr3.append(4)
    elif len(arr) == 2:
        arr3.append(5)
    else:
        arr3.append(6)
    # 최소    
    if len(arr2) == 6:
        arr3.append(1)
    elif len(arr2) == 5:
        arr3.append(2)
    elif len(arr2) == 4:
        arr3.append(3)
    elif len(arr2) == 3:
        arr3.append(4)
    elif len(arr2) == 2:
        arr3.append(5)
    else:
        arr3.append(6)
    return arr3    
