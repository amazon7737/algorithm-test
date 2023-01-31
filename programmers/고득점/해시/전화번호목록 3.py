def solution(phone_book):
    #print("234" in "12345")
    #print(phone_book[2] in phone_book[1])
    #phone_book.sort()
    #answer = True
    #for j in range(len(phone_book)):
        #a = phone_book[j]
        
    #    for i in range(1, len(phone_book)):
    #        if phone_book[j] in phone_book[i]:
    #            if phone_book[j] == phone_book[i]:
     #               pass
     #           else:
     #               answer = False
                    #print("answer: ", answer)
    #                break
    #   	if answer == False:
    #        break
    #return answer
    # -----------
    
    # 답
    phone_book.sort()
    for i in range(len(phone_book)-1):
        if phone_book[i] == phone_book[i+1][:len(phone_book[i])]:
            return False
    return True    
