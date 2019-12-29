from pprint import pprint
def grammarExtract(filename):
    fp = open(filename,'r')
    N,G,T = [],[],[]
    for line in fp.readlines():
        A = line.split(' -> ')
        if A[0] not in N: N.append(A[0])
        string = ''.join(A[1][i] for i in range(len(A[1])-1))
        G.append([A[0],string])
        for i in range(len(string)):
            if ord(string[i]) <= 64 or ord(string[i]) >= 91:
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
                if j1 != h-1:
                    trial = trial + perm[j1+1] + '.'
                    trial = trial + ''.join(perm[i1] for i1 in range(j1+2,h))
                else: trial = trial + '.'
                R.append(trial); R.append(B[2])
                if R not in S[i]: S[i].append(R)
        elif A[1][j+1] in T: # Scanner portion of the handler
            print("Scanner initiated")
            print("S until now: ->")
            pprint(S)
            try:
                print(i,string[i],A[1][j+1])
                if string[i] == A[1][j+1]:
                    R = []; R.append(A[0]); perm = A[1]; h = len(perm)
                    trial = ''.join(perm[i1] for i1 in range(j))
                    if j != h-1:
                        trial = trial + perm[j+1] + '.'
                        trial = trial + ''.join(perm[i1] for i1 in range(j+2,h))
                    else: trial = trial + '.'
                    R.append(trial); R.append(A[2])
                    print("New item in the state",R,R not in S[i+1])
                    if R not in S[i+1]:
                        S[i+1].append(R)
                        print("Scanner handled")
                        print("S after the change: ->")
                        pprint(S)
            except:
                R = []; R.append(A[0]); perm = A[1]; h = len(perm)
                trial = ''.join(perm[i1] for i1 in range(j))
                if j != h-1:
                    trial = trial + perm[j+1] + '.'
                    trial = trial + ''.join(perm[i1] for i1 in range(j+2,h))
                else: trial = trial + '.'
                R.append(trial); R.append(A[2])
                print("New item in the state",R,R not in S[i])
                if R not in S[i]:
                    S[i].append(R)
                    print("Scanner handled")
                    print("S after the change: ->")
                    pprint(S)
        elif A[1][j+1] in N: # Predictor portion of the handler
            for P in G:
                if P[0] == A[1][j+1]:
                    R = []; R.append(P[0]); e = '.'+P[1]
                    R.append(e); R.append(i)
                    if R not in S[i]: S[i].append(R)
def earleyAlgorithm(filename,string):
    print("Welcome to the execution of Earley's algorithm")
    (N,G,T) = grammarExtract(filename)
    n = len(string)
    S = [[] for i in range(n+1)]
    R = []; R.append(G[0][0]); R.append('.'+G[0][1]); R.append(0)
    S[0].append(R)
    for i in range(n+1): handler(S,i,N,G,T,string)
    R = []; R.append(G[0][0]); R.append(G[0][1]+'.'); R.append(0)
    print(R)
    if R in S[n]: return True
    else: return False
print(earleyAlgorithm('example3.txt','xpxsx'))
def lexer_early(string):
    return earleyAlgorithm('lexerEarly.txt',string)
def parser_early(string):
    return earleyAlgorithm(filename,string)