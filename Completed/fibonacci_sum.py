def fibonacci_sum(n):
    x = 0
    y = 1
    fib = []
    index = []
    fib.append(x)
    fib.append(y)
    counter = x + y
    
    while counter <= n:
        fib.append(counter)
        x = y
        y = counter
        counter = x + y
    answer = 0
    fib.sort(reverse=True)
   
    while True:
        for i in fib:
            if answer + i > n:
                continue
            else:
                index.append(i)
                answer = answer + i
                if answer == n:
                    break
                fib.remove(i)
        if answer == n:
            break
        
    return index

def fibonacci_sum(n):
    x = 0
    y = 1
    fibo = []
    val = []
    fibo.append(x)
    fibo.append(y)
    next = x + y
    
    while next <= n:
        fibo.append(next)
        x = y
        y = next
        next = x + y
    answer = 0
    fibo.sort(reverse=True)
   
    while True:
        for i in fibo:
            if answer + i > n:
                continue
            else:
                val.append(i)
                answer = answer + i
                if answer == n:
                    break
                fibo.remove(i)
        if answer == n:
            break

    return val