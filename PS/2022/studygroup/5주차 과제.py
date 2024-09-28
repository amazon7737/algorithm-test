#5주차 과제

#1번 문제

import sys

def push(x):
    stack.append(x)

def pop():
    y = stack.pop()
    return y if stack else -1

def size():
    return len(stack)

def empty():
    return 0 if stack else 1

def top():
    return stack[-1] if stack else -1

stack = []

N = int(input())

for _ in range(N):
    input_1 = sys.stdin.readline().rstrip().split()
    cmd = input_1[0]
    if cmd == "push":
        push(input_1[1])
    elif cmd == "pop":
        print(pop())
    elif cmd == "size":
        print(size())
    elif cmd == "empty":
        print(empty())
    elif cmd == "top":
        print(top())
        
#2번 문제


#3번 문제

n = int(input())
cnt = 0
stack = []
result = []

for _ in range(n):
    a = int(input())
    if a > cnt:
        while cnt != a:
            cnt += 1
            stack.append(cnt)
            result.append("+")
        stack.pop()
        result.append("-")
    else:
        b = stack.pop()
        result.append("-")
        if b != a:
            result = ["NO"]
            break
            
print("\n".join(result))

#4번 문제

from collections import deque

n = int(input())
q = deque([i for i in range(1, n+1)])

while len(q) != 1:
    q.popleft()
    q.append(q.popleft())
print(q.pop())

#5번 문제

from collections import deque
import sys

n = int(input())
num = deque()
for _ in range(n):
    com = list(sys.stdin.readline().split())

    if com[0] == 'push_front':
        num.appendleft(com[1])
    elif com[0] == 'push_back':
        num.append(com[1])
    elif com[0] == 'pop_front':
        if len(num) == 0:
            print("-1")
        else: print(num.popleft())
    elif com[0] == 'pop_back':
        if len(num) == 0:
            print("-1")
        else: print(num.pop())
    elif com[0] == 'size':
        print(len(num))
    elif com[0] == 'empty':
        if len(num) == 0:
            print("1")
        else: print("0")
    elif com[0] == 'front':
        if len(num) == 0:
            print("-1")
        else: print(num[0])
    elif com[0] == 'back':
        if len(num) == 0:
            print("-1")
        else: print(num[-1])
        
