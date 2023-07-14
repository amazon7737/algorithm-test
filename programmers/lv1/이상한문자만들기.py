def solution(s):
    # ! 
    
    # split(' ') vs split() 차이?
    a =''; b = s.split(' '); arr =[]
    print(b)
    for i in b:
        for j in range(len(i)):
            if j % 2 == 0:
                a += i[j].upper()
            else:    
                a += i[j].lower()
        a +=' '
    return a[0:-1]   
    
