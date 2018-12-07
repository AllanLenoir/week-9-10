def f(a):
    if a < 0:
        return -1
    n = a    
    while n > 0:
        if n % 2 == 0 : # n is even
            n = n // 2
        elif n==1:
            return 1
        else:
            n = 3 * n + 1
    return 0


print(f(-1), "/",f(0),"/", f(1),"/", f(2),"/", f(10),"/", f(100))
