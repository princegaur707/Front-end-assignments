from math import ceil, sqrt
def genprimes(x,n):
    primes=[True]*(n+1)
    primes[0]=primes[1]=False
    for p in range(2,ceil(sqrt(n))):
        if primes[p]==True:
            for i in range(p*p,n+1,p):
                primes[i]=False
    for i in range(x,n+1):
        if primes[i]==True:
            print(i,end=" ")
while True:
    x,n=map(int,input("\nEnter number:   ").split())
    genprimes(x,n)