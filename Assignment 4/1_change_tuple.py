#As tuple is immutable so we have two options either we go to 
#conversion or we can simply print the o/p which we require
def changelast(list1,value):
    print([tp[:-1] +(value,) for tp in list1])
changelast([(10, 20, 40), (40, 50, 60), (70, 80, 90)],100)
changelast([(10, 20, 40), (40, 50, 60), (70, 80, 90)],200)