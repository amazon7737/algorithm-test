def solution(n):
    a = "수";b="박";c=''
	# n = 1 ->  수  n = 2 -> 수박
    for i in range(1, n+1):
        if i % 2 == 0:
            c +=b
        else:
            c += a
    return c
