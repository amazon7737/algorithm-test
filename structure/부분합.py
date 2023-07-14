import sys

# 입력부
t = int(sys.stdin.readline())
n = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split()))
m = int(sys.stdin.readline())
b = list(map(int, sys.stdin.readline().split()))

# 배열 A의 부분합을 담을 key_set
key_set = []
ans = 0

# A의 모든 쌍을 돌면서 부분합 결과를 key_set에 담는다
# 이때 만일 A의 부분합이 temp라면 temp를 key_set에 담지 않고
# B의 부분합이 t- temp가 되어야 매칭이 가능하므로 t - temp를 담아준다
for i in range(n):
    temp = a[i]
    key_set.append(t - temp)
    for j in range(i + 1, n):
        temp += a[j]
        key_set.append(t - temp)

# 사전 생성 후, 가능한 쌍들의 갯수를 저장한다
compare = dict().fromkeys(key_set,0)
for i in key_set:
    compare[i] += 1

for i in range(m):
    temp = b[i]
    # 반드시 복수개 이상으로 이루어지지 않더라도 가능한 경우가 존재하기에
    # 1개로만 이루어진 경우를 우선적으로 체크한다
    # 다만, 이때 compare에 대응되는 값이 없다면 KeyError를 리턴하므로 예외처리를 한다
    try:
        ans += compare[temp]
    except:
        pass
    # 복수개 이상으로 이루어진 부분합의 대응여부를 확인한다
    for j in range(i + 1, m):
        temp += b[j]
        try:
            ans += compare[temp]
        except:
            pass

print(ans)
