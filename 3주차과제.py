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

#3
N_2 = int(input())
list__  = [list(input().split())for _ in range(N_2)]

