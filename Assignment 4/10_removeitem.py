def removeitem(set1,list1):
    for i in list1:
        set1.remove(i)
    print("updated set:  ",set1)
removeitem({1,2,3,4,5},[4,5])