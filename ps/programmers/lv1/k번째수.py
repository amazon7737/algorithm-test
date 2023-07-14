# good
def solution(array, commands):
    arr=[]
    for idx, num in enumerate(commands):
        print(num[2])
        a = sorted(array[num[0]-1:num[1]])
        arr.append(a[num[2]-1])
    return arr
