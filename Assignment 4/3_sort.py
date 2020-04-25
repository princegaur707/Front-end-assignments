def sorttuple(list1):
    print(sorted(list1,key=lambda x:float(x[1]),reverse=True))
sorttuple([('item1', '12.20'), ('item2', '15.10'), ('item3', '24.5')])