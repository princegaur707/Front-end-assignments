while True:
    t = list(tuple(map(int,input().split())) for r in range(int(input('Enter Rows : ')))) 
    print(f"Original Tuple:  {t}")
    t.sort(key=lambda x:[x[1],x[0]])   #IF the second element of tuple will be same then first element will be considered
    print(f"Sorted Tuple:     {t}")