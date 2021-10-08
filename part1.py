

def combinations(tuple1):
    mul=1
    for i in tuple1:
        mul=mul*i
    
    print("combinations",tuple1,"is",mul)
    
   

combinations((2,3))
combinations((3,7,4))
combinations((2,3,4,5))
