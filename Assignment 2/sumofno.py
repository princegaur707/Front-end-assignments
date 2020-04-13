def sum(n):
    s=0
    for i in range(1,n+1):
        s+=i*i 
    return s
while True:
    n=int(input("Enter number:    "))
    print(sum(n))
    