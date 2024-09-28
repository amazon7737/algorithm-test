# 규칙성을 파악해서 경우의수를 줄여나가야되는 문제.

def solution(brown, yellow):
    # 카펫의 가로 세로 크기 예측
    # 노란색 격자는 무조건 정중앙
    # 한쪽줄 격자는 갈색으로 가득찬것을 봣음.
    arr=[]
    for i in range(1, yellow+1):
        if yellow % i == 0:
            if (int(yellow/i)*2) + i*2 + 4 == brown:
                arr.append(int(yellow/i)+2)
                arr.append(i+2)
                
                return sorted(arr, reverse=True)
