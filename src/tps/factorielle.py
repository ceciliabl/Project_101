def factorielle(n):
    if  n is None or n<=0:
        return "erreur"
        #raise Exception("erreur recommencer")
    if n==1:
        return 1

    result=n*factorielle(n-1)
    return result

def syracuse(n):
    suite=[n]
    if n==1:
        return

    while(n!=1):
        if n%2==0:
            result = n/2
        else:
            result = 3*n+1
        suite.append(result)
        n=result
    return(suite)

def decroissant(n):
    if n==0 :
        print (n)
    else:
        print (decroissant (n-1))
        print (n)
    return

print("toot")
