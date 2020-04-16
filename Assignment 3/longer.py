while True:
    nums=list(map(str,input("Enter list elements:   ").split()))
    n=int(input("Enter n:  "))
    for i in nums:
        if len(i)>n:
            print(i)
    