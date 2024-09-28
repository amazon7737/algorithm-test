def solution(s):
    answer = 0;cnt=0;cnt2=0
    
    for i in s:
        print(i)
        if cnt == cnt2:
            answer += 1
            k=i
        if k == i:
            cnt += 1
        else:
            cnt2 += 1
        print("cnt:", cnt)    
        print("cnt2:", cnt2)
    return answer    
