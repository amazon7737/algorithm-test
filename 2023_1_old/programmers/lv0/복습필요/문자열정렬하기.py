def solution(my_string):
    arr = []
    for i in range(len(my_string)):
        try:
            
            arr.append(int(my_string[i]))
        except:
            pass
    arr.sort()	
    return arr
