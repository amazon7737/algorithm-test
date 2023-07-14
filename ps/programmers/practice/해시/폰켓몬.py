from collections import deque
def solution(nums):
    nums = deque(nums)
    phone = {}; result = {}
    number = len(nums) // 2
    ketmon = list(set(nums))
    for i in range(len(ketmon)):
        phone[ketmon[i]] = 0
        result[ketmon[i]] = 0
    while len(nums)!=0:
        plus = nums.popleft()
        phone[plus] += 1
    #print(phone)    
    #print("number:",number)
    arr=[]
    while number != 0 :
        for i in ketmon:
            if phone[i] -1 >=0 and number != 0:
                phone[i] -= 1
                if result[i] == 0:
                    result[i] += 1
                    
                number-=1
                    
        #print("number:", number)
        #print("phone:",phone)
        #print("result:",result)
    cnt = 0    
    for i in ketmon:
        if result[i] == 1:
            cnt += 1
    return cnt        
            
