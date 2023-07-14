def solution(s):
    # 스택으로 간단히 풀리는 문제
    # 문자열 같은 알파벳 2개 붙어있으면 -> 그 둘을 제거 -> 앞뒤로 문자열 이어붙이기
    # baabaa -> bb aa -> aa -> ??
    # aa 제거 -> bb 제거 -> aa 제거 -> 아무것도 없으니까 return 1
    # 더이상 제거가 불가능하면 return 0
    arr=[]
    for i in s:
        if len(arr) == 0:
            arr.append(i)
        elif arr[-1] == i:
            arr.pop()
        else:
            arr.append(i)
    if len(arr) == 0:
        return 1
    return 0
