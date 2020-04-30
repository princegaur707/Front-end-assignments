def inrange(low,num,high):
    return low<=num<=high
while True:
    low,num,high=map(int,input("Enter low,num,high :       ").split())
    print(inrange(low,num,high))