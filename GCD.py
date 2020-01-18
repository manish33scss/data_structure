def gcd(m,n):
    fn=[]
    for i in range(1,n+1):
        if(n%i)==0:
            fn.append(i)
    fm=[]
    for j in range(1,m+1):
        if (m%j)==0:
            fm.append(j)
    common=[]
    for f in fn:
        if f in fm:
            common.append(f)
    return(common[-1])


m=int(input("enter value of m"))
n=int(input("enter value of n"))

print("ans"+ str(gcd(m,n)))
