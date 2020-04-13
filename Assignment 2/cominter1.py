def compountinterest(p,r,t):
    result=p*(pow((1+r/(n*100)),n*t))
    return result
while True:
    p,r,n,t=map(float,input("Enter p,r,n,t  :  ").split())
    print(compountinterest(p,r,t))
