from collections import deque

def solution(priorities, location):
    alpha = "A";priorities_alpha=deque();cnt=1;priorities = deque(priorities)
   #알파벳 생성 
    for i in range(len(priorities)):
        priorities_alpha.append(chr(ord(alpha)+i))
        # alpha_array:
        # ["A", "B", "C", "D"]
    # 목표하는 알파벳    
    result_alpha = priorities_alpha[location]
    #print(result_alpha)
    # "C"    
    # 0 제외하니까 런타임 에러뜸
    while len(priorities) > 0:
        number = priorities.popleft()
        alpha = priorities_alpha.popleft()
        
        #print(number, alpha)
        if len(priorities) > 0:
            if number < max(priorities):
                priorities.append(number)
                priorities_alpha.append(alpha)
            else:
                if alpha == result_alpha:
                    return cnt
                
                cnt += 1
            
        #print(priorities, priorities_alpha)
        # 우선순위가 같다면 , ,, 그냥 리턴 안해서 예외 케이스 3개 생겼었음
        # while 안에서 리턴 안당하고 나오면 return 해줘야함.
    return cnt    
            
    

