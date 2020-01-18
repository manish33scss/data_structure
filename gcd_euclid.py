def gcd(p,q):
    if p<q:
        (p,q)=(q,p)
    if (p%q)==0:
        return(q)
    else:
        diff=p-q
        return(gcd(max(q,diff),min(q,diff)))
        
p=int(input("enter value of p"))
q=int(input("enter value of q"))

print("ans__gcd __ Euclidean   "+ str(gcd(p,q)))
        
