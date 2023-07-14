def solution(my_string):
    alpha_ = ["A", "B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
    alpha = ["a", "b","c","d","e","f","g", "h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    
    arr = ""
    for i in range(len(my_string)):
        if my_string[i] in alpha_:
            arr += alpha[alpha_.index(my_string[i])]
        if my_string[i] not in alpha_:
            arr += my_string[i]
    arr2 = []
    for i in range(len(arr)):
        arr2.append(arr[i])
        arr2.sort()
    print(arr2)
    arr = ""
    for i in range(len(arr2)):
        arr += arr2[i]
        
    return arr
