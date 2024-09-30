from egzP1atesty import runtests 

def recursion(S, M, D, lc):
    y = float('inf')
    x = float('inf')
    #print(S)
    for l in D:
        if M[l][1] == S:
            return lc+1
        elif len(M[l][1]) < len(S):
            if M[l][1] == S[0:len(M[l][1])]:
                #print("fiut" ,S, S[len(M[l][1]):])
                y = min(y, recursion(S[len(M[l][1]):], M, D, lc+1))
    return min(y, x)

def titanic( W, M, D ):
    print(D)
    for r in D:
        print(M[r])
    print(W)

    S = ""
    for l in W:
        for l2, m in M:
            if l==l2: S += m
    print(S)
    print(S[0:4])

    return 0

runtests ( titanic, recursion=True )