
def syracuse(n):
    return syracusehelper (n,[])

def syracusehelper(n,l):
    l.append(n)
    if n==1:
        return l
        return len(l)
        return max(l)

    #while(n!=1):
    elif n%2==0:
        return syracusehelper( n/2,l)

    else:
        return syracusehelper (3*n+1, l)


def fibonacci1(n):
    suite=[]
    if n==0 or n==1:
        suite.append(1)
    else:
        suite.append()
