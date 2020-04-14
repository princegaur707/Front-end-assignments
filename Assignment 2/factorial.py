dict1={}
def factorial(x):
    if x in dict1:
        return dict1[x]
    if x==0: # This will be required as it is the end condition adding this to dict1 will not help as we are calling factorial(0)
        return 1
    else:
        dict1[x]=x*factorial(x-1)
        return dict1[x]
        
while True:
    try:
        n=int(input("Enter num:"))
        print(factorial(n))
    except:
        print("Inalid input!")
        break