#1번 문제
# H - Index

N = int(input())

H = [0]*N

H = list(map(int, input().split()))

H.sort()

print(H[2])
