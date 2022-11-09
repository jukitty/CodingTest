def solution(array):
    answer = 0
    max_count = 0
    counter = set(array)
    
    for c in counter:
        if max_count < array.count(c):
            max_count = array.count(c)
            answer = c
            
        elif max_count == array.count(c):
            answer = -1 
    return answer