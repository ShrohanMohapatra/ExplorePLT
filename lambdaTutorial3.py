# Some uses of lambda calculus
from random import randint 
gcd = lambda a,b: a if b == 0 else gcd(b,a%b)
reverseMod = lambda d,e,n: d if (e*d)%n == 1 else reverseMod(d-1,e,n)
actualReverseMod = lambda e,n: reverseMod(n-1,e,n)
randGen = lambda x: randint(1,50)
fact = lambda x: 1 if x == 0 else x*fact(x-1)
pGen = lambda x: ((fact(randGen(x))%(randGen(x)+1))/randGen(x)) * (randGen(x)-1) + 2
nGen = lambda x: pGen(x)*pGen(pGen(x))
PhiNGen = lambda x: (pGen(x)-1)*(pGen(pGen(x))-1)
eGen = lambda x: pGen(x)
dGen = lambda x: actualReverseMod(eGen(x),PhiNGen(x))
encryption = lambda m,x: (m**eGen(x))%nGen(x)
print(encryption(2,3))