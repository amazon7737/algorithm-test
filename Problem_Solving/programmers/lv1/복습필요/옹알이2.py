def solution(babbling):

# 문제상황을 제대로 이해못함
# 연속된 글자만 없으면 전부 발음 가능한 상황이니까 그것외에 플러스1 씩 하면 답이된다.
# 케이스 3개 못함
    arr = ["aya", "ye", "woo", "ma"]
    # 네가지 발음과 네가지 발음을 조합해서 만들 수 잇는 발음 밖에못함
    # 연속해서 같은 발음하는 것을 어려워함
    #
    arr2 = [];arr3=[];arr4=[];cnt=0
    
    for i in range(len(arr)):
        for j in range(len(arr)):
            if arr[i] == arr[j]:
                pass
            else:
                arr2.append(arr[i]+ arr[j])
                
    for i in range(len(arr)):
        for j in range(len(arr)):
            for k in range(len(arr)):
                if arr[i] == arr[j] or arr[j] == arr[k]:
                    pass
                else:
                    arr3.append(arr[i] + arr[j] + arr[k])
                    
                
    for i in range(len(arr)):            
        for j in range(len(arr)):
            for k in range(len(arr)):
                for s in range(len(arr)):
                    if arr[i] == arr[j] or arr[k] == arr[s] or arr[j] == arr[k]:
                        pass
                    else:
                        arr4.append(arr[i]+arr[j]+arr[k]+arr[s])
                

    print("arr:", arr)            
    print("arr2:", arr2)        
    print("arr3:", arr3)
    print("arr4:", arr4)
    for i in range(len(babbling)):
        if babbling[i] in arr:
            cnt += 1
        if babbling[i] in arr3:
            cnt += 1
        if babbling[i] in arr2:
            cnt += 1
        if babbling[i] in arr4:
            cnt += 1
    return cnt

# 답안
# replace, strip() 사용

# 옹알이 ( 2)
answer = 0

for i in babbling: # babbling
    print("i:",i)
    for j in ['aya', 'ye', 'woo', 'ma']: # 첫번째 발음
        if j*2 not in i: #
            i = i.replace(j, ' ')
            print("i =", i)

    if len(i.strip())==0: # 시작, 끝부분의 공백을 다 없애도 아무것도 없으면
        answer += 1 # answer 에 카운트 1
print("answer:",answer)

