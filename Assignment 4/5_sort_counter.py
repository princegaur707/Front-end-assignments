from collections import Counter
def sortcounter(list1):
    list1=Counter(list1)
    print(list1.most_common())
sortcounter({'Math':81, 'Physics':83, 'Chemistry':87})