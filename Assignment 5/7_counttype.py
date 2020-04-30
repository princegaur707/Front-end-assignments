def counttype(string):
    countU=0
    countL=0
    for i in string:
        if i.islower():
            countL+=1
        if i.isupper():
            countU+=1
    return countU,countL
while True:
    string=input("Enter string:   ")
    countU,countL=counttype(string)
    print("No. of Uppercase characters:    ",countU)
    print("No. of lowercase characters:    ",countL)