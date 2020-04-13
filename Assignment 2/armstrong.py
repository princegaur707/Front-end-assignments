#sum of cube of its digits is equal to same number
def armstrong(n):
    x=n
    s=0
    while n:
        t=n%10
        s+=t**3
        n//=10
    return x==s
while True:
    n=int(input("Enter number:    "))
    print(armstrong(n))
