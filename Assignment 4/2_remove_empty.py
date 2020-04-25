def remove_empty(list1):
    list1=[i for i in list1 if i]
    print(list1)
remove_empty([(), (), ('',), ('a', 'b'), ('a', 'b', 'c'), ('d')])

