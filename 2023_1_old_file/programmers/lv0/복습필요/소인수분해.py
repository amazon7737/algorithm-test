def solution(n):
    arr = []
    i = 2
    while i <= n:
        
        if n % i == 0:
            arr.append(i)
            n = n // i
        else:
            i += 1
            
    #if arr == []:
    #    return n
    #arr.sort()        
    return sorted(list(set(arr)))

# 테스트케이스 만점 안나오던 이유
# 정렬이 안된상태로 제출되었음 -> sort 하고 list에 씌우는거 X

