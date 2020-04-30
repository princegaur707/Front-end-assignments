def returneven(nums):
    return [i for i in nums if i%2==0]
while True:
    nums=list(map(int,input("Enter list elements:   ").split()))
    print(returneven(nums))