# 1번문제

N = int(input("입력"))
En = list(map(int, input().split()))
mini = min(En)
maxi = max(En)

index = En.index(mini)
index2 = En.index(maxi)

print(En[index], " ", En[index2])

# 2번문제


total = 0
score = 0

go = int(input())
    
for j in range(0, go):
    right = list(input())
    
        
    total = 0
    score = 0
    
    for i in range(0, len(right)):
        if right[i] == "O":
            score = score +1
            total = total + score
            
        else:
            score = 0
            total = total + score
    print(right, " = ", total)        
                        
#3번문제

a = int(input()) # 번수
for k in range(0, a):
    list_1 = list(map(int, input().split())) # list_1[0] => 개수임

    aver = 0
    aver_tot = 0
    right = 0
    list_2 = list([0]*len(list_1))
    for a in range(1, len(list_1)):

        aver = aver + list_1[a]
        aver_tot = aver/list_1[0]
    
        b = 0
    for b in range(1, len(list_1)):
        if list_1[b] <= aver_tot:
            list_2[b] = 1
        
        else:
            continue

    no = list_2.count(1) # 평균 이하의 수 개수

    x = 100/list_1[0]
    y = no*x
    z = 100 - y
    print(format(z, '.3f'), "%")
    
#4번문제

n = int(input())
for i in range(1, (n+1)):
    if i == 1:
        print((' '* 3) + "*")
    else:
        print((' ' * (n-i)) + "*" + (' ' * ((i*2)-3))+"*")
   
#5번문제

    