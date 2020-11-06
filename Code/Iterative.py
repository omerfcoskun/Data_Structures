

print("N: ")
N=int(input())
fib1 = 0

fib2 = 1

fibonacci = [fib1,fib2]
for i in range(N):


    fib1,fib2 = fib2,fib1 + fib2

    fibonacci.append(fib2)

print(fibonacci)

