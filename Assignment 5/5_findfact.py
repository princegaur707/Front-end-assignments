def findfact(num):
    if num==0:
        return 1
    return findfact(num-1)*num
while True:
    num=int(input("Enter number:    "))
    print(findfact(num))