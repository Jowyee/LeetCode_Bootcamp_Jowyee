def myAtoi(s: str) -> int:
    INT_MIN = -2**31
    INT_MAX = 2**31 - 1
    
    n = len(s)
    i = 0
    sign = 1 
    result = 0
    
    while i < n and s[i] == ' ':
        i += 1
    
    if i < n and (s[i] == '+' or s[i] == '-'):
        sign = -1 if s[i] == '-' else 1
        i += 1
    
    while i < n and s[i].isdigit():
        digit = int(s[i])
        if result > INT_MAX // 10 or (result == INT_MAX // 10 and digit > INT_MAX % 10):
            return INT_MAX if sign == 1 else INT_MIN
        result = result * 10 + digit
        i += 1
    
    return sign * result