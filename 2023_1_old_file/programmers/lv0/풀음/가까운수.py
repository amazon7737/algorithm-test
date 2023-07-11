def solution(array, n):
    arr = []; array.sort()
    for i in range(len(array)):
        arr.append(abs(n - array[i]))
	
    return array[arr.index(min(arr))]
