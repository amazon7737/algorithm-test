# 간단한 스택으로 생각
def solution(board, moves):
    arr=[];cnt=0
    # 0은 빈칸
    # 
    # board 담긴 배열 , 인형을 집기위해  크레인을 작동시킨 위치? -> moves
    for move in moves:
        for i in range(len(board)):
            if board[i][move-1] != 0:
                arr.append(board[i][move-1])
                board[i][move-1]=0           
                if len(arr) > 1:
                    if arr[-1] == arr[-2]:
                        arr.pop();arr.pop()
                        cnt += 2
                break               
    return cnt
