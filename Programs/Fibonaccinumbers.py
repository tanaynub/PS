
def even_fibonacci_sum(n):
    n1 = 1 #Fn-2
    n2 = 1 #Fn-1
    sum = 0
    while True :
        t = n1 + n2 
        if t >= n: return sum
        if t % 2 == 0: sum += t
        n2= n1
        n1 = t

    
