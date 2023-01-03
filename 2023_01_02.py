#숨어있는 숫자의 덧셈 (2)

arr = re.findall(r"[0-9]+", my_string )


# 문자열 밀기
def solution(A, B):
    count = 0
    while count != len(A):
        if A == B:
            return count
        A = A[-1] + A[:-1]
        count += 1
        
    return -1    



