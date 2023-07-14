def solution(my_string):
    arr = ['a', 'b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    arr2 = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    result = ''
    for i in range(len(my_string)):
        for j in range(len(arr)):
            if my_string[i] == arr[j]:
                result += arr2[j]
                break
            elif my_string[i] == arr2[j]:
                result += arr[j]
                break
    return result
