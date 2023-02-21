# 딕셔너리 , 람다를 활용해서 자료형 원하는대로 바꾸기

dict_ = {}

# 고른 원소 / 배열의 총 개수 를 이용하여 계속 빠지면서 계산된다
# 배열의 총 개수
cnt = len(stages)

# 배열에 뽑을게 있다면, 딕셔너리에 첫번째 칸부터 고른원소 / 배열의 총개수를 집어넣기
for i in range(1, N+1):
    if cnt != 0:
        dict_[i] = (stages.count(i)/cnt)
        # 집어넣고 나서 총 개수에서 뽑은 개수 만큼을 빼기
        cnt -= stages.count(i)
    else:
        # 배열에 뽑을게 없다면 딕셔너리 그 위치에는 0을 집어넣기
        dict_[i] = 0

# 정렬 내림차순 안에 딕셔너리를         
print(sorted(dict_, key=lambda x: dict_[x], reverse = True))    
