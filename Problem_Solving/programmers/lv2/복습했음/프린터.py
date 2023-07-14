
from collections import deque
def solution(priorities, location):
    answer = 0

    d = deque([(v,i) for i,v in enumerate(priorities)])

    while len(d):
        item = d.popleft()
        if d and max(d)[0] > item[0]:
            d.append(item)
        else:
            answer += 1
            if item[1] == location:
                break
    return answer




    # 다시 풀어보앗지만 완전히 못풀음

    from collections import deque

def solution(priorities, location):
    # priorities : 문서의 중요도
    # location : 현재 대기목록의 어떤 위치에 있는지 알려줌.

    priorities = deque(priorities)
    cnt=0

    #for i in range(location):
    #    priorities.append(priorities.popleft())

    #print("priorities:",priorities)

    while True:
        doc = priorities.popleft()
        if priorities and max(priorities) > doc:
            priorities.append(doc)
        else:
            cnt += 1
            if doc == location:
                break
        print("priorities:", priorities)
        print(doc)
        print("cnt:",cnt)



