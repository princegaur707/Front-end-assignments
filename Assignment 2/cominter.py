#https://www.indiabix.com/aptitude/compound-interest/formulas
# Formula of compound interest: 
#     A= P+(1+r/n)^nt
#     A-> Final amount
#     P-> Principal amount
#     r-> rate of interest
#     n-> no. of times interest applied per time period
#     t-> no. of times period elasped
    
def compoundinterest(p,r,n,t):
    return p*(1+(r/(100*n)))**(n*t)
while True:
    p,r,n,t=map(float,input("Enter values of p,r,n,t:     ").split())
    print(compoundinterest(p,r,n,t))