
def solution(ingredient):
    cnt=0;arr=[]
    # 야채 빵 빵 야채 고기 빵 야채 고기 빵
   # 빵 - 야채 - 고기 - 빵 
	# 상수가 포장하는 햄버거의 개수
    # 1 : 빵 , 2: 야채, 3 : 고기
    # 빵 - 야채 - 고기 - 빵 이 되는 순간 pop?
    
    for i in ingredient:
        arr.append(i)
        #print(arr[-4:])
        if arr[-4:] == [1,2,3,1]:
            cnt += 1
            del arr[-4:]
    return cnt


    # pop 으로 풀고 싶엇지만 방법이 떠오르지 않앗다
    # a:i+1 로 슬라이싱해서 할려고했지만 중첩 for문으로 시간초과 발생
    # -4: 인덱스를 이용해서 뒤에서부터 슬라이싱하여 보여주는 방법을 생각못했다.
