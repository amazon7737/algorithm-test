def solution(k, score):
    arr = [];arr2=[]
    for i in range(0, len(score)):
        if len(arr) < k:
            arr.append(score[i])
            arr.sort(reverse = True)
        else:
            if arr[-1] < score[i]:
                arr.append(score[i])
                arr.sort(reverse =True)
        #        print("arr111:",arr)
                arr.pop()
        #print("arr:",arr)        
        arr2.append(min(arr))
    return arr2
