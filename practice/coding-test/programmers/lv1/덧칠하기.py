from collections import deque

def solution(n, m, section):
    
    dict = {}
    
    for i in range(1, n+1):
        dict[i] = 0
        
    # 시작지점
    cnt=1
    paint = section[0]
    
    section2 = deque(section)
    
    result =0
    
    # 벽에서 벗어나는 경우
    for i in range(1, len(section)):
        
        # 벽을 넘어선 경우?
        if(section[i] - paint >=m):
            
            #dict[number+ i] += 1
            
            cnt += 1    
            paint = section[i]    
        
   # 최소 횟수를 리턴
    return cnt
