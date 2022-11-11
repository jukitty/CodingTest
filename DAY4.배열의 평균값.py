def solution(numbers):
    answer = 0
    sum = 0
    avg = 0
    
    for i in range(0,len(numbers),1):
        sum += numbers[i]
        
    avg = sum/len(numbers)
    answer = avg
    
    return answer