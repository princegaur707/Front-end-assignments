def simpleinterest(p,r,t):
    s=p+p*r*t
    return s
while True:
    p,r,t=map(float,input("Enter p,r,t:    ").split())
    print(simpleinterest(p,r,t))
    print(p(1.0+r*t))