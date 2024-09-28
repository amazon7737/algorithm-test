import math
def solution(n):
    print(int(math.sqrt(n)))
    
    if int(math.sqrt(n)) == math.sqrt(n):
        return (int(math.sqrt(n))+1)**2
    else:
        return -1
