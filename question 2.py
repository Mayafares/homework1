D_N=int(input("Enter your Decimal Number: "))
l=[] 
while D_N>0 :
    l.append(D_N%2)         
    D_N=D_N//2
l.reverse()  
i=0  
while i<len(l):
    print(l[i] , end="")
    i=i+1