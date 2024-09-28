#1
N = int(input())
list_ = list(map(int, input()))

x = 0
for i in range(0, len(list_)):
    x = x + list_[i]

print(x)

#2
pr = 0
H = []
for i in range(5):
    H = input()
    f = 0
    f.append(float(H))
    k = 0
    
    for j in range(1, len(f)):
        pr = k - f
        print(pr)

        
#3

for x in range(5):
    Hist = list(map(int, input().split()))

    y = 0
    if Hist[y] == Hist[y+1] and Hist[y] == Hist[y+2] and Hist[y+1] == Hist[y+2]:
        print("Equilateral")

    elif Hist[y] == Hist[y+1] or Hist[y] == Hist[y+2] or Hist[y+1] == Hist[y+2]:
        print("Isosceles")

    elif Hist[y] != Hist[y+1] and Hist[y] != Hist[y+2] and Hist[y+1] != Hist[y+2]:
        print("Scalene")

    else:
        print("Invalid")