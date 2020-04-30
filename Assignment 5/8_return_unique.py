def returnunique(nums):
    return list(set(nums))
while True:
    nums=list(map(int,input("Enter list elements:     ").split(',')))
    print(returnunique(nums))