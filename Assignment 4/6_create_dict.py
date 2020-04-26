from collections import defaultdict
def createdict(list1,list2):
    dict1=defaultdict(set) #we cannot use dict here as it cannot support this functionality
    for key,value in zip(list1,list2):
        dict1[key]=value
    print(dict1)
createdict(['Class-V', 'Class-VI', 'Class-VII', 'Class-VIII'], [1, 2, 2, 3])