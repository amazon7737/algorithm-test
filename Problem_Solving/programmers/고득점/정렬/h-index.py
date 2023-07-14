# 오답...

def solution(citations):
    arr =  []
    arr2 = []
    arr3 = []
    arr = citations
    arr.sort()
    n = len(arr)
    
    # h찾기
    # arr2 : 인용된 논문
    # arr3 : 인용되지 못한 논문
    
    # 0회 이상 인용된 논문의 수는?
    # 1회 이상 인용된 논문의 수는?
    # 2회 이상..
    for i in range(n):
        count = 0
        for j in range(n):
            if arr[j] >= i:
                count += 1
        arr2.append(count)    
    
    for i in range(n):
        if arr2[i] == arr[i]:
            return arr[i]
    print("arr2: ",arr2)
    print("arr3:", arr3)
    # n 편중 h번 이상 인용된 논문 h편 이상 -> 나머지 논문 h번 이하 인용 h의 최댓값
    
    return arr3[0]


# 해설

# 오름차순 풀이

def solution(citations):
  citations.sort()
  for idx, citation in enumerate(citations):
    if citation >= len(citations) - idx:
      return len(citations) - idx
  return 0

# 내림차순 출력

def solution(citations):
  citations.sort(reverse = True)
  for idx, citation in enumerate(citations):
    if idx >= citation:
      return idx
  return len(citations)

# 최고 많이 인용된 횟수 부터 시작해서 수가 내려가면서 검수한다
# 5편이니까 5편을 인용했는지 0번째 논문부터 비교를 시작한다 만약 5편 이상이라면?
# 인용된 논문 수를 그대로 리턴
