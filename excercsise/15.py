def fibonaci(n):
    if n <= 0:
        return []
    if n == 1:
        return [0]
    if n ==2 :
        return [0,1]
    fib_arr = [0,1]
    for i in range(2, n):
        next_fib = fib_arr[-1] + fib_arr[-2]
        fib_arr.append(next_fib)
    return fib_arr
print(fibonaci(5))