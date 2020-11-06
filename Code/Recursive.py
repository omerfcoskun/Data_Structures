
print("N :")
N=int(input())

def Fibonacci(pos):
    if pos <= 1:
        return 0
    if pos == 2:
        return 1
    fib1 = Fibonacci(pos - 1)
    fib2 = Fibonacci(pos - 2)
    fibn = fib1 + fib2
    return fibn

for i in range(1,N):
    wanted = Fibonacci(i)
    print(wanted)
