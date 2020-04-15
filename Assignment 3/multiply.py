import numpy
while True:
    nums=map(int,input("Enter numbers:   ").split())
    r=numpy.prod(nums)
    print(r)