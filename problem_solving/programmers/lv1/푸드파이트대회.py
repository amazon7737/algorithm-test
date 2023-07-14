def solution(food):
    # !
    # 물 0 -> 중앙
    a = '' 
    for i in range(1, len(food)):
        a+= str(i)*(food[i]//2)
    b = ''.join(reversed(list(a)))
    return a+'0'+b
  
  # 규칙성 찾기 / 쓸만한 자료구조 찾기 / 파이썬 기능 찾기 / dp로 풀리나? / 무식하게 
