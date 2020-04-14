#print fibonacci till number with memoization
fib={}
def fibonacci(n):
    if n in fib:
        return fib[n]
    if(n==0):
        return 0
    if(n==1):
        return 1
    else:
        fib[n]= fibonacci(n-1)+fibonacci(n-2)
        return fib[n]
while True:
    try:
        n=int(input("\nEnter number:   "))
        for i in range(n):
            print(fibonacci(i),end=" ")
    except:
        print("Invalid input!")
        break