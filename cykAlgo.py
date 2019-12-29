from pprint import pprint
def grammarExtract(filename):
    fp = open(filename,'r')
    N,R,U = [],[],[]
    for line in fp.readlines():
        A = line.split(' -> ')
        if A[0] not in N: N.append(A[0])
        string = ''.join(A[1][i] for i in range(len(A[1])-1))
        if len(string) == 1: U.append([A[0],string])
        if len(string) == 2: R.append([A[0],string])
    fp.close()
    return (N,R,U)
(N,R,U) = grammarExtract('example1.txt')
print('N = '+str(N))
print('R = '+str(R))
print('U = '+str(U))
def CYKalgo(filename,string):
    (N,R,U) = grammarExtract(filename)
    n = len(string)
    r = len(N)
    
print(CYKalgo('example1.txt','aaa'))