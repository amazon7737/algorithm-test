def solution(numbers):
    arr = []
    
    a_list = list(map(str, numbers))
    
    a_list.sort(key = lambda x:x*3, reverse = True)
    print(a_list)
    answer = ''
    answer = answer.join(a_list)
    print(answer)
