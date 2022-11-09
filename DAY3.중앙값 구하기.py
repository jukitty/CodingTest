def solution(array):
    answer = 0
    median = 0
    index = 0
    
    array.sort()
    
    if len(array)%2==0:
        index = len(array)//2
        median = (array[index] + array[index-1])/2
        answer = median    
    else:
        index = len(array)//2
        median = array[index]
        answer = median
        
    return answer