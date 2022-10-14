

#10809
s = str(input())
a = [chr(i) for i in range(97, 122+1)]
for i in a:
  try:
    print(s.index(i), end = ' ')
  except:
    print(-1, end = ' ')

