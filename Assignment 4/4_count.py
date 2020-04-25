def countelements(list1):
    count=0
    for i in list1:
        if isinstance(i,tuple):
            break
        count+=1
    print(count)
countelements([1,2,3,4,(5,6),7,8])