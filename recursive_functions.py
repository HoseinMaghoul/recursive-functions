# Fibonacci numbers: [1, 1, 2, 3, 5, 8, 13, 21, .....]
# algorithm: n * n

def fib(n):
    if n == 1 or n == 0:
        return  1
    return  fib(n-1) + fib(n-2)

print(fib(7))

#_________________________________________
# algorithm: n
memory = {0:1, 1:1}
def fib(n):
    if n not in memory:
        memory[n] = fib(n-1) + fib(n-2)
        return  memory[n]