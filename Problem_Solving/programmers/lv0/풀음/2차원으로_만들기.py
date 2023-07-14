def solution(num_list, n):
    arr = [[0]*n for _ in range(len(num_list) // n)]
    # n 매개변수 -> n개 씩 나눠서 2차원배열로 변경
    k = 0
    for i in range(len(num_list)):
        for j in range(n):
            try:
                arr[i][j] = num_list[k] 
                k += 1
            except IndexError:
                pass
            
    return arr  
