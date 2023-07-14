# 테스트케이스 일부 런타임 에러 발생
# 효율성을 얼마나 바라는지 모르겟다... 잘 푼거 같은데

def solution(s):
    answer=[]
    s = s.split(' ')
    for i in s:
            answer.append(i[0].upper() + i[1:len(i)].lower())
    return ' '.join(answer)

# 새로운 해설 Capitalize() 사용
# 내장함수로 효율성 강제 상승
def solution(s):
    answer = ''
    s=s.split(' ')
    for i in range(len(s)):
        # capitalize 내장함수를 사용하면 첫 문자가 알파벳일 경우 대문자로 만들고
        # 두번째 문자부터는 자동으로 소문자로 만든다
        # 첫 문자가 알파벳이 아니면 그대로 리턴한다
        s[i]=s[i].capitalize()
    answer=' '.join(s)
    return answer
