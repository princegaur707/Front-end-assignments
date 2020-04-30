from math import ceil,sqrt
def chkprime(num):
    if num<=1:
        return False
    if num<=3:
        return True
    if num%2==0 or num%3==0:
        return False
    for i in range(5,ceil(sqrt(num))+1,6):
        if num%i==0 or num%(i+2)==0:
            return False
    return True
while True:
    num=int(input("Enter number:    "))
    print(chkprime(num))