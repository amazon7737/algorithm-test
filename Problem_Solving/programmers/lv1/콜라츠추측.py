def solution(num):
    cnt = 0
    for _ in range(500):
        if num == 1:
            break
            
        if num % 2 == 0:
            print("1:",num)
            num = num // 2
            cnt += 1
            print(num)
        else:
            print("2:",num)
            num = (num * 3) + 1
            cnt += 1
            print(num)
            
        if cnt == 500 and num != 1:
            return -1
    return cnt    
        
