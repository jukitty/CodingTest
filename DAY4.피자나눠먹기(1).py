def solution(n):
    answer = 1
  
    if n/7 > 0:
        if n%7 != 0:
            answer = int(n/7)+1
        else:
            answer = int(n/7)
    
    elif n/7 == 0:
        answer = 1
    
    return answer

# answer//7