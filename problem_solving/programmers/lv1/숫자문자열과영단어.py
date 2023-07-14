def solution(s):
    arr = ['zero', 'one', 'two', 'three', 'four','five','six','seven','eight','nine']
    a = ''
    for num, i in enumerate(arr):
        
        if i in s:
            s= s.replace(i, str(num))
        a = s    
    return int(a)
