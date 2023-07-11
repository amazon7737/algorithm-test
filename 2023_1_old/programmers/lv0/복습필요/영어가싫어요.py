def solution(numbers):
    arr = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight" , "nine"]
    
    for i, num in enumerate(arr):
        print("i: ", i)
        print("num: ", num)
        numbers = numbers.replace(num, str(i))
    return int(numbers)  
