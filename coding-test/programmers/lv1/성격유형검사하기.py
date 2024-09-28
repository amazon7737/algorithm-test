def solution(survey, choices):
    # 라이언 R , 튜브 T
    # 콘 C , 프로도 F
    # 제이지 J , 무지 M
    # 어피치 A , 네오 N
    
    # 1 2 3 4 5 6 7
    # 3 2 1 0 1 2 3
    dict_ = {"R":0, "T":0, "C":0, "F":0, "J":0, "M":0, "A":0, "N":0}
    location_ = [1,2,3,4,5,6,7]
    score_ = [3,2,1,0,1,2,3]
    arr=[];a=''
    # 만약 점수가 동일하면 사전순으로
    
    for i in range(len(choices)):
        if choices[i] <= 3:
            dict_[survey[i][0]] += score_[location_.index(choices[i])]
        elif choices[i] >= 5:
            dict_[survey[i][1]] += score_[location_.index(choices[i])]
    #print("dict_:",dict_)        
    #for i in range(len(dict_)):
    if dict_['R'] > dict_['T']:
        a += 'R'
    elif dict_['R'] < dict_['T']:
        a += 'T'
    else:
        a += 'R'

    if dict_['C'] > dict_['F']:
        a += 'C'
    elif dict_['C'] < dict_['F']:
        a += 'F'
    else:
        a += 'C'

    if dict_['J'] > dict_['M']:
        a += 'J'
    elif dict_['J'] < dict_['M']:
        a += 'M'
    else:
        a += 'J'

    if dict_['A'] > dict_['N']:
        a += 'A'
    elif dict_['A'] < dict_['N']:
        a += 'N'
    else:
        a += 'A'
    return a
