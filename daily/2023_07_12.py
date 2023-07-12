# 프로그래머스 : 자릿수 더하기

def solution(n):
    arr=[]
    n = str(n)
    for i in range(len(n)):
        arr.append(int(n[i]))
    return sum(arr)  

# 프로그래머스 : 문자열 내 p와 y의 개수

def solution(s):
    s = s.lower()
    if s.count('p') == s.count('y'):
        return True
    elif s.count('p') != s.count('y'):
        return False
    return True

# 프로그래머스 : 달리기 경주

def solution(players, callings):
    # players : 1등부터 현재 등수대로 담긴 배열
    # callings : 해설진이 부른 이름을 담은 배열
    # 경주가 끝낫을때 선수들의 이름 1등부터 순서대로 배열
    NametoNumber = {}; NumbertoName={}
    # NametoNumber  {'mumu': 1, 'soe': 2, 'poe': 3, 'kai': 4, 'mine': 5} 
    # NumbertoName {1: 'mumu', 2: 'soe', 3: 'poe', 4: 'kai', 5: 'mine'}

    for i in range(0, len(players)):
        NametoNumber[players[i]] = i+1
    for i in range(len(players)):
        NumbertoName[i+1] = players[i]
    #print(NametoNumber)    
    for i in range(len(callings)):
        #print(NumbertoName[NametoNumber[callings[i]]])
        
        
        rank = NametoNumber[callings[i]]
        name2 = NumbertoName[rank-1]
        rank2 = NametoNumber[name2]
        name = NumbertoName[rank]
        
        NametoNumber[callings[i]] = rank2
        NametoNumber[name2] = rank
        
        NumbertoName[rank] = name2
        NumbertoName[rank2] = name
    NumbertoName = sorted(list(NumbertoName.items()) , key = lambda x:x[0])
    arr=[]
    for i in range(len(NumbertoName)):
        arr.append(NumbertoName[i][1])
        print(arr)

