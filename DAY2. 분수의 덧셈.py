def gcd(a,b):
    if a % b == 0:
        return b
    else:
        return gcd(b,a%b)

def solution(denum1, num1, denum2, num2):
    answer = []
    
    x = denum1*num2 + denum2*num1
    y = num1 * num2
    g = gcd(x,y)
    
    answer = [x//g, y//g]
    
    return answer