


def prime(n):
    if n>1:
        for i in range(2,int(n/2)+1):
            if n%i==0:
                print("False")
                break
        else:
                print("True")
    else:
         print("False")
    



prime(7)
prime(56963)
prime(5151512515524)
