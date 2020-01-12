# Solving for the factorial problem
fact = lambda x: 1 if x==0 else x*fact(x-1)
print(fact(9))
# Solving for the problem of tower of Hanoi
T = lambda n,A,B,C: 1 if n == 1 else T(1,A,C,B)+T(n-1,A,B,C)+T(n-1,C,B,A)
A, B, C = None,None,None
print(T(3,A,B,C))
# Solving the problem by means of Minsky registers
swap = lambda x, y: (y,x)
def move(A,B,nA,nB): A[nA], B[nB] = swap(A[nA],B[nB])
A = [1,2,3,4,5,6]
B = [0,0,0,0,0,0]
move(A,B,len(A)-1,0)
print(A,B)