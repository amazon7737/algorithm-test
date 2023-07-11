def solution(keyinput, board):
    arr = [0, 0]
    
    print(keyinput)
    
    for i in range(len(keyinput)):
        if keyinput[i] == "left":
            if arr[0] -1 < -(board[0] // 2):
                pass
            else:
                arr[0] -= 1
        elif keyinput[i] == "right":
            if arr[0] + 1 > board[0]//2:
                pass
            else:
                arr[0] += 1
        elif keyinput[i] == "up":
            if arr[1] + 1 > board[1]//2:
                pass
            else:
                arr[1] += 1
        elif keyinput[i] == "down":
            if arr[1] -1 < -(board[1]//2):
                pass
            else:
                arr[1] -= 1
    return arr
