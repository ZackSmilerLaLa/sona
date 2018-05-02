def rev(wight,high):
    return wight*high
def aev(wight,high):
    return .5*wight*high

n = int(input("rev = 1 and   aev = 2 please Enter the No."))
w = int(input("input wight:"))
h = int(input("input high:"))

if  n==1:
    print(rev(w,h))

elif n==2:
    print(aev(w,h))
else:
    print("Erorr Number!!!!")
    
     
