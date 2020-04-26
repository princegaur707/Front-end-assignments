def sumofdict(dict1):
    s=0
    for key in dict1:
        s+=dict1[key]
    print(s) 
sumofdict({'Class-V': 1, 'Class-VI': 2, 'Class-VII': 2, 'Class-VIII': 3})