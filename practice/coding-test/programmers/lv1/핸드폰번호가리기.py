def solution(phone_number):
    return "*"*(len(phone_number)-4)+phone_number[-4:-1]+phone_number[-1]


###
# 2023.08.03(목)
def solution(phone_number):
    return (len(phone_number) - len(phone_number[-4:]))*"*" + phone_number[-4:]
