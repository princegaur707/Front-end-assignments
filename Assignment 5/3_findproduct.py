import numpy
def findproduct(nums):
    return numpy.prod(nums)
while True:
    nums=list(map(int,input("Enter list elements:  ").split()))
    print(findproduct(nums))