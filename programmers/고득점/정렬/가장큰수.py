def solution(numbers):
    arr = []
    
    a_list = list(map(str, numbers))
    
    a_list.sort(key = lambda x:x*3, reverse = True)
    answer = ''
    answer = answer.join(a_list)
    return str(int(answer))
