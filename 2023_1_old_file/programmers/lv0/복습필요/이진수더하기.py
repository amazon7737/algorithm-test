# 케이스 3개 통과못함 
def solution(bin1, bin2):
    a = ""; number1=0;number2=0
    j = 0
    
    # bin1 이진수 -> 10진수
    for i in range(len(bin1)-1, -1, -1):
        if int(bin1[i]) == 1:
            number1 += int(2**j)
            
        elif int(bin1[i]) == 0:
            pass
        j += 1
        
	# bin2 이진수 -> 10진수
    j = 0    
    for i in range(len(bin2)-1, -1, -1):
        if int(bin2[i]) == 1:
            number2 += int(2**j)
        elif int(bin2[i]) == 0:
            pass
        j += 1
        
        
    arr = [] ; arr2 = []
    a = number1 + number2 ; c = ""
    #print("a:", a)
    
    # 이진수들
    for i in range(11):
        arr.append(2**i)
        
    # 10진수 -> 2진수
    if len(str(a)) == 1:
        for i in range(, -1, -1):
            if a - arr[i] < 0:
                c += "0"
            else:
                c += "1"
                a = a - arr[i]
    else:    
        for i in range(len(bin1), -1, -1):
            if a - arr[i] < 0:
                c += "0"
            else:
                c += "1"
                a = a - arr[i]
    
    return str(c)
            # c 가 결과
            # a 는 10진수 합한거
            # number1 , number 2진수 -> 10진수 변환한거


# bin 을 이용한 풀이 (생각해냇지만 사용법을 몰랏음)

def solution(bin1, bin2):
    a = int(bin1, 2)
    b = int(bin2, 2)
    return bin(a+b)[2:]

   # 찾아보고 새로 짜봄 (인덱스를 이용해서 ob 빼고 출력)
   #( int 기능 새로알았음... 저기 넣으면 되는거 몰랐음)
