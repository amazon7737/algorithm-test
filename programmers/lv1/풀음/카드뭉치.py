from collections import deque
def solution(cards1, cards2, goal):
# 5분도안걸림
    cards1=deque(cards1);cards2=deque(cards2)
    # cards1
    # cards2 
    # cards1 , cards2로 goal를 만들기
    
    print(type(goal))
    
    for i in range(len(goal)):
        if goal[i] in cards1:
            a = cards1.popleft()
            if a == goal[i]:
                pass
            else:
                return "No"
        elif goal[i] in cards2:
            b = cards2.popleft()
            if b == goal[i]:
                pass
            else:
                return "No"
            
    return "Yes"        

