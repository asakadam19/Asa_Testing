def fib(n):
    
    fib_list = [0,1]
    if n == 1:
        return [0]
    if n == 2:
        return fib_list
    next_val = 0
    
    for i in range(2,n):
        next_val = fib_list[i-1] + fib_list[i-2]
        fib_list.append(next_val)
        
    
    return fib_list[n-1]


n = 11

print(fib(n))