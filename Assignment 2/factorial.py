dict1={}
def factorial(x):
    if x in dict1:
        return dict1[x]
    if x==0:
        return 1
    else:
        dict1[x]=x*factorial(x-1)
        return dict1[x]
        
while True:
    n=int(input("Enter num:"))
    print(factorial(n))