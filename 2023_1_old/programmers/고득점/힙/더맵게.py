#테스트케이스는 다맞춤. 하지만 효율성 테스트 0점.. 기본배열 말고 heap공간을 이용하면 시간복잡도, 공간복잡도를 줄이나봄.
# 맨처음 for문에 if 문 조건 맞으면 break 방식을 사용했는데 return -1 조건을 생각안해서 테스트케이스 4개가 틀렸음.
def solution(scoville, K):
    arr = []
    count = 0
    arr = scoville
    
    
    while min(arr) < K:
        try:
            arr.sort();a = arr[0] + (arr[1]*2);arr.pop(0);arr[0]=a;count+=1
        except IndexError: # 까먹고 -1 return 할 경우를 뺌.
            return -1
            
    return count

# 효율성 테스트를 고려한 코드
# https://itholic.github.io/kata-more-spicy/

# heapq 라는 라이브러리를 활용한 heap 코드

def solution(scoville, k):
  heap = []
  for num in scoville:
    heapq.heappush(heap, num)

  mix_cnt = 0
  while heap[0] < k:
    try:
      heapq.heappush(heap, heapq.heappop(heap) + (heapq.heappop(heap) * 2))
    except IndexError:
      return -1
    mix_cnt += 1

  return mix_cnt

# 복습이 필요할듯 싶다
