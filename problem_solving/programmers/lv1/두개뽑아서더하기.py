from collections import deque
def solution(numbers):
    arr = []
    numbers2 = deque(numbers)
    for i in range(len(numbers2)):
        a = numbers2.pop()
        
        for j in range(len(numbers2)):
            arr.append(numbers2[j]+a)
        
        numbers2.appendleft(a)
    return sorted(list(set(arr)))
