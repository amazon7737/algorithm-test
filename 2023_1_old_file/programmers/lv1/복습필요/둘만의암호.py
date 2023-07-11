# 다 못풀음 배열로 풀려고 했으나 실패 ord, chr 을 사용하면 된다는것은 알겠는데 자동화에 대해서는 생각하지 못함
# !

def solution(s, skip, index):
    # 각 되어야되는 알파벳
    # 알파벳이 skip 에 포함되어있으면 count 세서 그만큼 index 추가하고 chr(ord) 더해서 배열에 다시 대입
    # i 번째 -1 번째들 모아서 join
    
    string_ = list(skip)
    arr=[[] * n for n in range(len(s))];arr3=[];arr4=[[] * n for n in range(len(s))]
    
    # --
    # arr 추가
    for j in range(len(s)):
        cnt = 0
        for i in range(index):
            cnt+=1
            a = chr(ord(s[j])+cnt)
            arr[j].append(a)
            print("arr:",arr)
    # --        
            
    #print(len(arr))        
    
    # -- arr 에 0 채우기
    for i in range(len(arr)):
        for j in range(len(arr)):
            if arr[i][j] in string_:
                arr[i][j] = '0'
                
    # --            
    # arr3 카운트
    for i in range(len(arr)):
        cnt = 0
        for j in range(len(arr)):
            if arr[i][j] == '0':
                cnt+=1
        arr3.append(cnt)
        
    # -- 
    # arr4
    for j in range(len(s)):
        cnt = 0
        for i in range(index):
            cnt+=1
            a = chr(ord(s[j])+cnt)
            arr4[j].append(a)
            print("arr4:",arr4)
    # --        
    # 인덱스 추가
    for i in range(len(arr)):
        if arr[i][j] == '0':
            arr4[i][j] = chr(ord(arr4[i][j])+1)
        else:
            arr4[i][j] = chr(ord(arr4[i][j])+arr3[i])
    print("arr4:",arr4)    


# 해설

def solution(s, skip, index):
    answer = ''
    skip = set(ord(w) for w in skip)
    #print(skip)
    
    for word in s:
        cnt = index ;word = ord(word)
        while cnt != 0:
            word += 1
            if word > ord('z'):
                word = word - ord('z') + ord('a') - 1
            if word in skip:
                continue
            # pass는 안되고 while 문에서는 continue
            cnt -= 1
        answer += chr(word)
        
    return answer    
