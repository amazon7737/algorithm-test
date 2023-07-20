result = 0
arr=[]
hap = 0
#아직 다 풀지 못함

# 문제 :
# 재귀함수는 이해했지만 문제 상황에 맞게 어떻게 더하고  빼야하는지
# 언제까지 더해야하는지 헷갈린다.
def solution(numbers, target):
    global hap
    index = 0
    
    #print(target)
    try:
        print("하하하")
        dfs(index, numbers)
    except IndexError:
        pass
#def dfs(index, numbers,  hap):
#    global result
#    if hap == target and index == len(numbers)-1:
        
#    	result+=1
#    print("hap:",hap)    
#    dfs(index+1, numbers, hap+numbers[index]*1)
#    dfs(index+1, numbers, hap+numbers[index]*-1)

def dfs(index, numbers):
    
    global result
    arr.append(numbers[index])
    hap+=numbers[index]

    if hap == target and index == len(numbers)-1:
        result += 1
        
    print("arr:",arr)
    print("hap:",hap)
    
    dfs(index+1, numbers)
    
  #  dfs(index+1, numbers)
    
    
    # visited = [False] * len(numbers)
        
    
#     if len(numbers) % 2 !=0:
#         graph = [[numbers[0]]]
#         graph.append([numbers[0], -numbers[0]])
#         for i in range(1, len(numbers)+1):
#             graph.append(graph[i]*2)
#             #print("graph:", graph)
#         dfs(graph, 1, visited)
    
# def dfs(graph, v, visited):    
#     # 첫번째 방문기록
#     visited[v] = True
#     print(v, end ='')
#     # 그래프 반복문
#     for i in graph[v]:
#     # 만약 방문하지 않았다면
#         if not visited[i]:
            
#     # 방문 기록 세우기
#             #visited[i] = True
#             dfs(graph, i , visited)
        
