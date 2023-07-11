def solution(sides):
    # !
    # 가장 긴 변의 길이 -> 다른 두변의 길이의 합보다 작아야함.
    # 두변의 길이 -> sides # 나머지 한변이 될수 있는 정수의 개수
    cnt = 0
    
    a = max(sides)
    b = min(sides)
    
    for i in range(a-b+1, a+1 ):
        cnt +=1
    for i in range(a+1, a+b):
        cnt +=1
    
    return cnt
