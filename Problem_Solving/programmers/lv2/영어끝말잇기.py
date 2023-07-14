def solution(n, words):
    used_words = []
    number, order = 0,0

    used_words.append(words[0])
    last_word = words[0][-1]
    for i in range(1,len(words)):
        if words[i] not in used_words and words[i][0] == last_word:
            used_words.append(words[i])
            last_word = words[i][-1]
        else:
            number = (i%n)+1
            order = (i//n)+1
            break

    return [number, order]
    # 1부터 n 까지 번호가 붙어있는 n명의 사람이 영어 끝말잇기
    # 1번부터 번호 순서대로 한사람씩 차례대로 단어를 말함
    # tank -> kick -> know ---
    # 3번사람이 말한 tank는 이미 등장한 단어 이므로 탈락
    
    # 사람의 수 n 과 사람들이 순서대로 말한 단어 words , 가장 먼저 탈락하는 사람의 번호 그 사람
    # 자신의 몇번째 차례에 탈락하는지를 구함 return 
    
    # 스택
#     arr2=[]
#     # arr 사람 , arr2 
#     arr=[0]*n;arr3=[]
#     arr2.append(words[0])
#     arr[0] += 1
#     # arr.index+1 // n -> 추가
#     for i in range(1,len(words)):
#         print("arr:",arr)
#         print("arr2:",arr2)
#         if arr2[-1][-1] == words[i][0]:
#             arr2.append(words[i]) # 단어 추가
#             arr[(len(arr2))//n-1] += 1 # 위치 맞춰서 + 1 카운트
#             print(len(arr2)//n-1) 
            
#         if arr2.count(words[i]) == 2:
#             arr3.append(len(arr2)//n) # 두개가 되는 순간 카운트 해주고 추가해주고 break
#             arr3.append(arr[len(arr2)//n-1])
#             break
#         elif arr2[-1][-1] != words[i][0]:
#             break
#     if arr3 == []:
#         return [0, 0]
#     print("arr3:",arr3)
#     return arr3

        
