def solution(clothes):
    # hash_map 에 headgear 나 eyewear 를 세준다..
    # 1. 옷을 종류별로 구분하기
    hash_map = {}
    for clothe, type in clothes:
        hash_map[type] = hash_map.get(type, 0) + 1
        print("clothe:", clothe)
        print("type: ", type)
        print("hash_map: ", hash_map)
        
    # 2. 입지 않는 경우를 추가하여 모든 조합 계산하기
    answer = 1
    for type in hash_map:
        # type 안에 hash_map 에 있는 'face' 이런것들이 자동으로 들어감
        # 
        answer *= (hash_map[type] + 1)
        print("hash_map2:", hash_map[type])
        print("answer: ",answer)
    
    # 3. 아무종류의 옷도 입지 않는 경우 제외하기
    return answer - 1

#print(solution([["crowmask", "face"], ["bluesunglasses", "face"], ["smoky_makeup", "face"]]))    
