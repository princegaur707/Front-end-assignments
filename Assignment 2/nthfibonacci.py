#nth fibonacci with memoization
fib={}
def nthfibonacci(n):
    if n in fib:
        return fib[n]
    if n==0:
        return 0
    if n==1:
        return 1
    fib[n]=nthfibonacci(n-1)+nthfibonacci(n-2)
    return fib[n]
while True:
    try:
        n=int(input("Enter number:    "))
        print(nthfibonacci(n-1))
    except:
        print("Invalid input!")
        break