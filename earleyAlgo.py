def equality(A,B):
    print(str(A))
    print(str(B))
    print("In-function equality",str(A) == str(B))
    return str(A) == str(B)
def grammarExtract(filename):
    fp = open(filename,'r')
    N,G,T = [],[],[]
    for line in fp.readlines():
        A = line.split(' -> ')
        if A[0] not in N: N.append(A[0])
        string = ''.join(A[1][i] for i in range(len(A[1])-1))
        G.append([A[0],string])
        for i in range(len(string)):
            if ord(string[i]) <= 64 and ord(string[i]) >= 91:
                if string[i] not in T: T.append(string[i])
    fp.close()
    return (N,G,T)
def handler(S,i,N,G,T,string):
    for A in S[i]:
        j = A[1].index('.')
        if j == len(A[1]) - 1: # Completer portion of the handler
            for B in S[A[2]]:
                R = []; R.append(B[0])
                perm = B[1]; h = len(perm); j1 = B[1].index('.')
                trial = ''.join(perm[i1] for i1 in range(j1))
                trial = trial + perm[j1+1] + '.'
                trial = trial + ''.join(perm[i1] for i1 in range(j1+2,h))
                R.append(trial); R.append(B[2])
                if R not in S[i]: S[i].append(R)
        elif A[1][j+1] in T: # Scanner portion of the handler
            if string[i+1] == A[1][j+1]:
                R = []; R.append(A[0]); perm = A[1]; h = len(perm)
                trial = ''.join(perm[i1] for i1 in range(j))
                trial = trial + perm[j+1] + '.'
                trial = trial + ''.join(perm[i1] for i1 in range(j+2,h))
                R.append(trial); R.append(A[2])
                if R not in S[i+1]: S[i+1].append(R)
        elif A[1][j+1] in N: # Predictor portion of the handler
            for P in G:
                if P[0] == A[1][j+1]:
                    R = []; R.append(P[0]); e = '.'+P[1]
                    R.append(e); R.append(i)
                    if R not in S[i]: S[i].append(R)
def earleyAlgorithm(filename,string):
    (N,G,T) = grammarExtract(filename)
    n = len(string)
    S = [[] for i in range(0,n+1)]
    R = []; R.append(G[0][0]); R.append('.'+G[0][1]); R.append(0)
    S[0].append(R)
    for i in range(0,n+1):
        print(i)
        while True:
            S1 = []
            for A in S: S1.append(A)
            handler(S,i,N,G,T,string)
            print("Equality",equality(S1,S))
            if equality(S1,S): break
        if len(S[i+1]) == 0: return False
    R = []; R.append(G[0][0]); R.append(G[0][1]+'.'); R.append(0)
    if R in S[n]: return True
    else: return False
print(earleyAlgorithm('example1.txt','aab'))