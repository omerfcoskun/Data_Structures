print("N :")
N=int(input())

def Fibonacci(pos):
    if pos == 1:
        return 0
    if pos == 2:
        return 1

    return Fibonacci(pos-1)+Fibonacci(pos-2)

for i in range(1,N):
    wanted = Fibonacci(i)
    print(wanted)

