def solution(numbers):
    answer = []
    
    for i in range(0,len(numbers),1):
        numbers[i] *= 2
    
    answer = numbers
    return answer