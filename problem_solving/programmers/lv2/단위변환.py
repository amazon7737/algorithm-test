from collections import deque

def solution(begin, target, words):
# answer 선언
  answer = 0

  # q 로 큐 선언
  q = deque()


# 제일 첫번째 begin 단어를 큐에 추가
  q.append([begin, 0])

  # words 갯수만큼 0을 가지고 있는 배열 선언
  V = [ 0 for i in range(len(words))]

# q에 있는 애들이 없어질때 까지 
  while q:

  # q에서 popleft 해서 word cnt 를 각각 구한다
    word, cnt = q.popleft()

    # word 와 target 문자가 같으면
    if word == target:
    # answer 안에 cnt를 넣기
      answer = cnt
      # 바로 break
      break
    # words 갯수만큼 반복문 
    for i in range(len(words)):

    # temp_cnt 선언
      temp_cnt = 0

      # v에 i번째가 없다면
      if not v[i]:

      # word 갯수만큼 for 반복문
        for j in range(len(word)):

        # word에 j번째와 words에 i,j번째가 다르면
          if word[j] != words[i][j]:

          # temp_cnt 카운트 + 1
            temp_cnt += 1
            # temp_cnt 가 1이면
        if temp_cnt == 1:
        # q에 words i번째와 cnt+1 추가
          q.append([words[i], cnt+ 1])
          # v에 i번째 1대입

