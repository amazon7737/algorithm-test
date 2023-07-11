def solution(n):
#     arr=[];arr2=[]
#     for i in range(1, n+1):
#         arr.append(i)
#         arr2.append(sum(arr))
    
#     for i in range(len(arr)):
#         try:
#             arr2.append(arr[i]+arr[i+1])
#         except IndexError:
#             pass
#     for i in range(len(arr)):
#         print(arr[i:])
#     print("arr:",arr)    
#     print("arr2:",arr2)
    return len([i  for i in range(1,n+1,2) if n % i is 0])
                
