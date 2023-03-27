# 정확성 44..

from collections import deque
def solution(people, limit):
    cnt = 0;boat=deque()
    people.sort()
    people = deque(people)
    boat.append(people.popleft())
    cnt += 1
    while people > 1:
        if boat[0] + people[0] <= limit and sum(boat) < limit:
            boat.append(people.popleft())
            
    #print("boat:",boat)        
    #print("people:",people)
    return cnt

## 답

from collections import deque

def solution(people, limit):
    answer = 0
    people = deque(sorted(people, reverse = True))
    
    while len(people) > 1:
        if people[0] + people[-1] <= limit: # 최댓값과 최솟값 묶어서 보트태움
            answer += 1
            people.pop()    #최소 빼내고
            people.popleft()    #최대 빼내고
        else:
            answer += 1
            people.popleft()
            
    if people:  #people에 1명 남아있는 경우 처리
        answer += 1
                
    return answer

## --
## 
def solution(people, limit) :
    answer = 0
    people.sort()

    a = 0
    b = len(people) - 1
    while a < b :
        if people[b] + people[a] <= limit :
            a += 1
            answer += 1
        b -= 1
    return len(people) - answer
