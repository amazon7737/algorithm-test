#1644
def primes(n):
	if n < 2:
		return [0]
	is_prime = [True] * (n+1)
	for i in range(2, n+1):
		if is_prime[i]:
			for j in range(i+i, n+1, i):
				is_prime[j] = False
	return [k for k in range(2, n+1) if is_prime[k]]

def solve():
	n = int(input())

	prime = primes(n)
	csum = [0]
	[csum.append(csum[i] + prime[i]) for i in range(len(prime))]

	answer = 0
	l, r = 0, 1

	while r <= len(prime):
		num = csum[r] - csum[l]
		if num == n:
			answer += 1
			l += 1
		elif num < n:
			r += 1
		else:
			l += 1

	print(answer)


solve()



```python
#2557

print("Hello World!")
```


```python
#1000

  1 a, b = map(int, input().split())
  2
  3 print(a + b)


```


```python
#2558

1 A = int(input())
3 B = int(input())
4
5 print(A + B)


```

```python
#10950

T = int(input())
for i in range(T):
  a ,b = map(int, input().split())
  print(a+b)




```


```python
#10951 ❌
while True:
	try:
		a, b = map(int, input().split())
		print(a+b)
	except EOFError:
		break


```

```python
#10952 ❌
while True:
	a, b = map(int , input().split())
	if a==0 and b==0:
		break
	print(a+b)

# if 조건문으로 필터링을 먼저주고 출력 순서를 바꿔야함
# 순서가 틀려서 틀렸음.
```

```python
#10953

T = int(input())

for _ in range(T):
	a, b = map(int, input().split(','))
	print(a+b)

# split 의 사용법을 이제야 알게되었다....


```


