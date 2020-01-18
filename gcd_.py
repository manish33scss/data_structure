def gcd(a,b):
    cn=[]
    for i in range(1,min(a,b)+1):
        if (a%i)==0 and (b%i)==0:
            cn.append(i)
    return(cn[-1])
a=int(input("enter value of m"))
b=int(input("enter value of n"))

print("ans"+ str(gcd(a,b)))
