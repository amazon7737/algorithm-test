#1번 문제
a = list(map(int,input("입력하세요")))

a.sort(reverse = True)

print(a)

#2번 문제
N = int(input()) # 개수
#for i in range(0, N):
 #   num_list = list(map(int, input()))
num_list = [int(input()) for _ in range(N)]

num_list.sort(reverse = False)

print(num_list)

#3번 문제
N = int(input())

list_1 = [[0]*2 for i in range(N)]
for i in range(N):
    age, name = input().split()
    age = int(age)
    list_1[i][0] = age
    list_1[i][1] = name


list_1.sort(key=lambda x:(x[0], x[1]))
for i in range(N):
    print(list_1[i])

#4번 문제
N = int(input())
list_1 = []
for i in range(N):
    list_1.append(input())

list_2 = list(set(list_1))

list_3 = []
for i in list_2:
    list_3.append((len(i), i))

x = sorted(list_3)

for b, list_1 in x:
    print(list_1)
    
#5번 문제

N = int(input())
b = []
for i in range(N):
    [x, y] = map(int, input().split())
    rev = [y, x]
    b.append(rev)
c = sorted(b)
for i in range(N):
    print(c[i][1], c[i][0])
