from collections import deque
def solution(number, limit, power):
    # 15번으로 지정된 기사단원 -> 약수 1 , 3 , 5 , 15 4개 -> 공격력이 4인 무기 구매
    # 이웃나라와의 협약 제한수치 3 , 제한수치를 초과한 기사가 사용할 무기 공격력 2라면, 
    # 공격력 1당 1kg의 철이 필요함 -> 철의 무게를 미리 계산
    # number : 기사단원 수 , limit 제한수치 , power 제한수치 초과한 기사가 써야할 공격력
    # 약수의 개수 -> 공격력
    arr=deque();arr2=deque()
    # div 반복문을 제곱근까지만 범위를 설정
    # 
    for i in range(1, number+1):
        cnt = 0
        for div in range(1, int(i**(1/2)+1)):
            if i % div == 0: 
                cnt += 1
                if div**2 != i: # 제곱이 되는 약수 중복 방지
                    cnt += 1
        arr2.append(cnt)
    for i in range(len(arr2)):
        if arr2[i] > limit:
            arr2[i] = power
    return sum(arr2)



