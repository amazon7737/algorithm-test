# 2742
N = int(input())
for i in range(N):  
    print(N)
    N = N -1
    
# 2739
N = int(input())
a = 1
for i in range(0, 9):
    print(N, '*', a, '=', N*a)
    a = a+1
    if a > 10:
        break
        
# 1924 _v
list_1 = list(map(int, input().split()))

# list_1[0] = x , list_1[1] = y
sum = 0 # 날의 총 합

a = [1, 3, 5, 7, 8, 10, 12]# 1, 3, 5, 7, 8, 10, 12 -> 31일까지

b = [4, 6, 9, 11] # 4, 6, 9, 11 -> 30일까지
# 2월은 28일까지
week = ['SUN', 'MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT']

for i in range(1, list_1[0]):
    if i in a :
        sum+=31
    elif i in b: 
        sum+=30
    elif i==2:
        sum+=28
sum+=list_1[1]
print(week[sum%7])
