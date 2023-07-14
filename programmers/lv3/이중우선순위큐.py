# 테스트케이스3 빼고 모두 통과
#from heapq import heappush, heappop
import heapq
from heapq import heappush
    # arr : 명령어들 모임
    # b : 글자들?
    # c : 숫자들 모임
def solution(operations):
    b=[];arr=[];c=[]
    for i in range(len(operations)):
        a = operations[i].split(" ");arr.append(a)
        heappush(b, a[1]);a = []
        print("b:",b)
    for i in range(len(arr)):    
        try:
            if ''.join(arr[i]) == "D1":
                c.remove(max(c))
            elif ''.join(arr[i]) == "D-1":
                c.remove(min(c))
            elif ''.join(arr[i][0]) == "I":
                c.append(int(b[i]))
                print("c:",c)
        except ValueError:
            pass
    c=list(set(c))            
    if c:
        return [heapq.nlargest(1, c)[0], heapq.nsmallest(1, c)[0]]
    else:
        return [0, 0]
# 반례를 찾지 못했다.
# 해설

import heapq

def solution(operations):
    heap = []

    for operation in operations:
        o = operation.split(' ') # 명령어 값 분리하여 저장

        # 명령어에 따라 처리하는 부분
        if o[0] == 'I': heapq.heappush(heap, int(o[1])) #명령어가 'I 숫자'인 경우
        else:
            if len(heap) > 0:
                # 명령어가 'D 1'인 경우
                if o[1] == '1': heap.pop(heap.index(heapq.nlargest(1, heap)[0]))
                # 명령어가 'D -1'인 경우
                else: heapq.heappop(heap)

    # 최대값, 최소값 리턴
    if heap: return [heapq.nlargest(1, heap)[0], heapq.nsmallest(1, heap)[0]]
    else: return [0, 0]
