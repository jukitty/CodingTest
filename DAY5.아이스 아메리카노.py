def solution(money):
    answer = []
    ame = money // 5500
    change = money - (ame*5500)
    answer.append(ame)
    answer.append(change)
    
    return answer