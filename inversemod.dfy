method inversemod(a: nat, n: nat) returns (t: nat, flag: bool)
requires a>0 && n>0;
ensures (!flag ==> t == 1) || (flag ==> (a*t)%n==1)
{
    var x := 0;
    while x<=a && (1+n*x)%a!=0
    invariant 0<=x<=a+1
    decreases (a-x) {
        x := x + 1;
    }
    if (x == a+1){
        flag := false; t := 1;
    }
    else{
        flag := true; t := (1+n*x)/a;
    }
}
function power(b: nat, e: nat): nat 
decreases e
{
    if e == 0 then 1 else b * power(b,e-1)
}
method expoBySquare(x:nat,n:nat) returns (p:nat)
requires n>=0
ensures p == power(x,n)
decreases *
{
    var N,q := n,x;
    p := 1;
    while N>=0
    decreases *
    {
        p := if N%2 == 0 then p else p*q;
        q := q * q;
        N := if N%2 == 0 then N/2 else (N-1)/2;
    }
}
function fact (n:nat) : nat
requires n >= 0
decreases n
{
    if n <= 0 then 1 else n*fact(n-1)
}
method Factorial(n: nat) returns (p: nat)
requires n>=0
ensures p == fact(n)
{
    var i : nat;
    i, p := 1,1;
    while i <= n
    invariant i<= n+1
    invariant p == fact(i-1)
    decreases n + 1 - i
    {
        p := p * i;
        i := i + 1;
    }
}
class primeRandomNumber{
    var xk: nat;
    constructor()
    ensures xk == 4;
    {
        xk := 4;
    }
    method primePRNG() returns (r: nat)
    modifies this
    ensures xk == (12*old(xk))%40
    ensures 40 < r < 1602
    {
        xk := (12*xk)%40;
        r  := xk*xk + xk + 41;
    }
}
method RSAencrypt (m: nat) returns (c: nat, flag: bool)
requires m>=0
decreases *
{
    var m1: nat; var f2: bool;
    var h := new primeRandomNumber();
    var p := h.primePRNG();
    var q := h.primePRNG();
    var n := p * q;
    var ph :=(p-1)*(q-1);
    var e := h.primePRNG();
    var d, f1 := inversemod(e,ph);
    if (f1){
        c := expoBySquare(m,e);
        c := c % n;
        m1 := expoBySquare(c,d);
        m1 := m1 % n;
        f2 := (m==m1);
        flag := f2 && f1;
    }else{
        flag := true;
        c := 9999;
    }
}