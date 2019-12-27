function fib(n: nat): nat
decreases n
{
    if n<=1 then n else fib(n-1)+fib(n-2)
}
method fibfast(n: nat) returns (c: nat)
requires n>=1;
ensures c==fib(n);
{
    var p := 0;
    c := 1;
    var i := 1;
    while(i<n)
    invariant 1<=i<=n
    invariant p == fib(i-1) && c == fib(i)
    decreases (n-i)
    {
        var new2 := p + c;
        p := c;
        c := new2;
        i := i + 1;
    }
}