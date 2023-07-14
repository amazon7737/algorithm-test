def solution(my_string):
    arr=[]
    for i in my_string:
        try:
            if int(i):
                arr.append(int(i))
        except ValueError:
            pass
    print(arr)        
    return sum(arr)
