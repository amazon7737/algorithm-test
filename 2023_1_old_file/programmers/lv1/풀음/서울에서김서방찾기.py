def solution(seoul):
    for i in range(len(seoul)):
        if seoul[i] == "Kim":
            a = seoul.index(seoul[i])
    return "김서방은"+" "+str(a)+"에 있다"
