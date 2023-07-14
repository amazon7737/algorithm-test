import math
def solution(n):
    # !
    
    # 시간 초과 3 + 효율성 X
    # 중첩 for 문 사용하면 시간초과로 사용불가
    #cnt = 0; arr = []
    #for i in range(2, n+1):
    #    for j in range(2, n+1):
    #        if i % j == 0:
    #            cnt += 1
    #    if cnt == 1:
    #        arr.append(i)
    #    cnt=0    
    #return len(arr)
    
    # 에라토스테네스의 체...
    
    # 다시 이해해보기
    
    cnt = [True]*(n+1)
    c = 0
    for i in range(2, int(math.sqrt(n))+1):
        if cnt[i]==True:
            for j in range(i+i, n+1, i):
                cnt[j] = False
                print("j: ", j, "cnt: ", cnt)
    for i in range(2, n+1):
        if cnt[i]:
            c += 1
    #print(c)        
    return c
