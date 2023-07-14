def solution(spell, dic):
    # 반례 : 문자들을 전부다 사용해야하는 경우
    # 어차피 중복된 문자를 사용하지 않는다는 조건이 있어서
    # 정렬해서 문자나오면 바로 return하도록해도됨.
	# !
    
    for a in dic:
        if sorted(a) == sorted(spell):
            return 1
        
    return 2    

