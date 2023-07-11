def solution(my_str, n):
    
    # n 씩 잘라서 저장하기
    return [my_str[i:i+n] for i in range(0, len(my_str), n)]
