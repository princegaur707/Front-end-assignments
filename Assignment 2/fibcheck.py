#fibonacci series till 20th : 0 1 1 2 3 5 8 13 21 34 55 89 144 233 377 610 987 1597 2584 4181
from math import ceil,sqrt
fib={}
def chkfibonacci(n):
    def builddict(n):
        for i in range(2,ceil(sqrt(n))):
            if(i<=0):
                return 0
            if(i==1):
                return 1
            else:
                fib[i]=builddict(n-1)+builddict(n-2)
    builddict(n)
    print(fib)
    if n in fib.values():
        return True
    return False 
while(True):
    n=int(input("\nEnter the number to check: "))
    print(chkfibonacci(n))