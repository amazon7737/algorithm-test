#1번문제

num1 = int(input("점수를 입력하세요"))

def database(num1):
    num2 = num1
    
    if 95 < num2 and 100 >= num2:
        print("A+")
    elif 90 < num2 and 95>=num2:
        print("A")
    elif 85 < num2 and 90>=num2:
        print("B+")
    elif 80 < num2 and 85>=num2:
        print("B")
    elif 75 < num2 and 80>=num2:
        print("C+")
    elif 70 < num2 and 75>=num2:
        print("C")
    elif 65 < num2 and 70>=num2:
        print("D+")
    elif 60 < num2 and 65>=num2:
        print("D")
    else:
        print("F")
    return 0

#2번문제

stop = int(input("초를 입력하세요"))

watch = int(stop/3600)
rest = stop - watch*3600
min = int(rest/60)
sec = rest%60 
print(watch,'시간',min,'분', sec,'초')

#3번문제

dot = list(map(int, input().split()))

x = dot[0]
y = dot[1]

if x >0 and y>0:
    print('1')
elif x<0 and y>0:
    print('2')
elif x<0 and y<0:
    print('3')
elif x>0 and y<0:
    print('4')
    
#4번문제

x = 1;y = 1;z = 1
for x in range(1, 10):
    for i in range(1, 10):    
        y = y+1
        z = x*y
        if y==10:
            y=1
            x=x+1
            z=x*y
        if x==10:
            break
        print(x, '*', y, '=', z)

#5번문제

N = int(input('입력'))
a=""
for j in range(0, N):
            a = a+"*"
for i in range(0, 2):
        print(a)
        a= a[0:N-2]
print("*")