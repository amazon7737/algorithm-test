# 그냥 완전히 다 계산해야하는 노가다문제
# isnumeric() 사용에 대해서 배울수 있다
# 배열과 캐싱을 이용해서 다 넣은다음
# 총 더하기로 계산
def solution(dartResult):
    # S 1 , D 2 , T 3
    # * 스타상 2배 , # 아차상 마이너스로 변화
    # ** 4배 , # *# -2배
    tmp = '';arr=[]

    for i in dartResult:
        print(i)
        if i.isnumeric():
            tmp += i
        elif i == "S":
            tmp = int(tmp) **1
            arr.append(tmp)
            tmp=''
        elif i == "D":
            tmp = int(tmp) **2
            arr.append(tmp)
            tmp=''
        elif i == "T":
            tmp = int(tmp) **3
            arr.append(tmp)
            tmp = ''
        elif i == "*":
            if len(arr) > 1:
                arr[-2] = arr[-2] * 2
                arr[-1] = arr[-1] * 2
            else:
                arr[-1] = arr[-1] * 2
            tmp *=2
        elif i == "#":
            arr[-1] = arr[-1] * -1
    return sum(arr)

