# Let us if the following expression runs in an infinite loop
# f = lambda x: x
# print(f)
# g = lambda f,x: f(f(x))
# print(g(f(1),1))
# TypeError: 'int' object is not callable
# f = lambda x: x(x)
# print(f(f))
# RecursionError: maximum recursion depth exceeded
# f = lambda x: x(x)(x)
# print(f(f))
# RecursionError: maximum recursion depth exceeded
from random import randint
churchNumeral = lambda N: lambda f: lambda x: (
    x if N == 0 else 1+f(churchNumeral(N-1)(f)(x))
)
f = lambda x: x
x1 = randint(0,100)
assert churchNumeral(x1)(f)(0) == f(x1)
add = lambda n: lambda m: lambda f: lambda x: (
    churchNumeral(n)(f)(churchNumeral(m)(f)(x))
)
x2,y2 = randint(0,100), randint(0,100)
assert add(x2)(y2)(f)(0) == x2+y2
mult = lambda n: lambda m: lambda f: lambda x: (
    churchNumeral(n)(churchNumeral(m)(f))(x)
)
actualMult = lambda n: lambda m: lambda f: lambda x: mult(n)(m-1)(f)(x)
x3,y3 = randint(0,100), randint(0,100)
assert x3*y3 == actualMult(x3)(y3)(f)(0)
exp = lambda n: lambda m: lambda f: lambda x: (
    churchNumeral(1)(f)(x) if n == 0
    else actualMult(m)(exp(n-1)(m)(f)(x))(f)(x)   
)
x4,y4 = randint(1,4), randint(1,4)
assert x4**y4 == exp(y4)(x4)(f)(0)
true = lambda x: lambda y: x
false = lambda x: lambda y: y
x1, y1 = randint(0,1), randint(0,1)
assert true(x1)(y1) == x1, false(x1)(y1) == y1
cond = lambda c: lambda t: lambda f: c(t)(f)
pair = lambda f: lambda s: lambda c: cond(c)(f)(s)
paircrement = lambda p: [
    pair(p)(add(1)(p)(f)(0))(true),
    pair(p)(add(1)(p)(f)(0))(false)
    ]
x1 = randint(0,1)
assert paircrement(x1) == [x1,x1+1]
predIter = lambda x: lambda n: (
    paircrement(x)[0] if paircrement(x)[1] == n
    else predIter(x+1)(n)
)
pred = lambda n: predIter(0)(n)
x1 = randint(0,10)
assert x1 - 1 == pred(x1)
zero = lambda n: true(1)(0) if n == churchNumeral(0)(f)(0) else false(1)(0)
x1 = randint(0,10)
assert zero(x1) if x1 == 0 else 1-zero(x1)