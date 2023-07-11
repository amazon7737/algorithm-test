def solution(n, lost, reserve):
    # n : 전체 학생의 수
    # lost : 도난당한 사람 번호
    # reserve 여분의 옷을 들고온 애들
   # 옷이 필요한 친구 
    arr = []
    lost.sort();reserve.sort()
    
    # arr : 여벌의 체육복을 가지고 있는 친구는 2로 표시, 안가지고 있는애는 0으로 표시
    # 1은 한벌만 가지고 있게
    # 스택으로 생각
          # 3 0 0 반례
    for i in range(1, n+1):
        if i in lost and i in reserve:
            arr.append(1)
        else:    
            if i in lost:
                arr.append(0)
            elif i in reserve:
                arr.append(2)
            else:
                arr.append(1)
    print(arr)        
    
    # 테스트 12  -> 반례 ! 0번째를 따로 계산하고
    if arr[0] == 0 and arr[1] == 2:
        arr[0] += 1
        arr[1] -= 1
    # 1번째부터 따로 계산    
    for i in range(1, len(arr)):
        try:
            if (arr[i] == 0 and arr[i-1] == 2):
                arr[i-1] -= 1
                arr[i] += 1
                print("arr1:",arr)
            elif (arr[i] == 0 and arr[i+1] == 2):        
                arr[i+1] -= 1
                arr [i] += 1 
                print("arr2:",arr)
        except IndexError:
            pass
    cnt =0       
   # print("arr",arr)
    
    for i in range(len(arr)):
        if arr[i] != 0:
            cnt += 1
    
    return cnt
