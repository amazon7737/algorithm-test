def solution(arr1, arr2):
    # !
    arr = []
    
    for i in range(len(arr1)):
        arr_sum = []
        for j in range(len(arr1[0])):
            arr_sum.append(arr1[i][j] + arr2[i][j])
        arr.append(arr_sum)    
    return arr    
