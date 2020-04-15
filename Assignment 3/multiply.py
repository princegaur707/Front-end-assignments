import numpy
while True:
    nums=list(map(int,input("Enter numbers:   ").split()))
    r=numpy.prod(nums)
    print(r)