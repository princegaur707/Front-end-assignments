from math import ceil, sqrt
def chkprime(n):
    if n<=1:
        return False
    if n<=3:
        return True
    if n%2==0 or n%3==0:
        return False
    for i in range(5,ceil(sqrt(n)+1),6):
        if n%i==o or n%(i+2)==0:
            return False
    return True
while True:
    n=int(input("Enter number:    "))
    print(chkprime(n))