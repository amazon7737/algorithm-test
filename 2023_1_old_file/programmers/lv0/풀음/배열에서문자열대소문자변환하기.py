
# 홀수 -> 대문자 , 짝수 -> 소문자
def solution(strArr):
    for i in range(len(strArr)):
        if (strArr.index(strArr[i]) % 2==0):
            strArr[i] = strArr[i].lower()
        else:
            strArr[i] = strArr[i].upper()
    return strArr
