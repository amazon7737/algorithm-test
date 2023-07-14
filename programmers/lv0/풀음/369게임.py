def solution(order):
    # 3 6 9
    count = 0
    a = str(order)
    for i in range(len(a)):
        if "3" == a[i]:
            count += 1
        elif "6" == a[i]:
            count += 1
        elif "9" == a[i]:
            count += 1
    return count 
