while True:
    nums=list(map(str,input("Enter numbers:  ").split()))
    count=0
    for i in nums:
        if len(i)>2 and i[0]==i[-1]:
            count+=1
    print(count)