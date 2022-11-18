def solution(price):
    answer = 0

    if 0 <= price < 100000:
        price = price
        
    elif 100000 <= price < 300000:
        price = price * 0.95
        
    elif 300000 <= price < 500000:
        price = price * 0.9
        
    elif 500000 <= price:
        price = price * 0.8
    
    answer = int(price)
    return answer