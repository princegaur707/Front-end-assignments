def cubesum(n):
    s=0
    for i in range(1,n+1):
        s+=i**3
    return s
while True:
    n=int(input("Enter number:    "))
    print(cubesum(n))
