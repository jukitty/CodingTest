def solution(slice, n):
    answer = 0
    for i in range(1,100,1):
        if n%slice == 0:
            answer = n/slice
        else:
            answer = n//slice + 1
        
    
    return answer