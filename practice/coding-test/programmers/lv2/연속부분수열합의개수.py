from collections import deque

# 문제 이해가 잘 안됫음
 
def solution(elements):
    answer = set()
    elements = deque(elements)
    for j in range(len(elements)):
        elements.rotate(1)
        for i in range(1,len(elements)):
            answer.add(sum(list(elements)[:i]))
    answer.add(sum(elements))
    return len(answer)
