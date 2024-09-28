def solution(absolutes, signs):
    boy = 123456789
    
    a = 0
    print(signs)
    for i in range(len(absolutes)):
        if signs[i] == True:
            a += absolutes[i]
        elif signs[i] == False:
            a -= absolutes[i]
    return a  
