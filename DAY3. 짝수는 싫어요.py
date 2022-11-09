def solution(n):
    answer = []
    n = n
    arr = [i for i in range(n)]
        
    for i in range(0,len(arr),1):
       
        if arr[i] % 2 != 0:
            answer.append(arr[i])
       
        else:
            continue
    
    if n%2 != 0:
        answer.append(n)

    return answer