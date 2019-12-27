method Swap(a: int, b: int) returns (x: int, y: int)
ensures x == b && y == a;
{
    x := b;
    y := a;
}
method Warn()
{
    var x;
    x := 1;
    assert x < 10;
    assert x < 100;
}
function fact(n : nat): nat
decreases n
{
    if n == 0 then 1 else n*fact(n-1)
}
method Factorial (n: nat) returns (p: nat)
requires n >= 0;
{
    var i: int;
    i, p := 1, 1;
    while (i <= n)
    invariant i <= n + 1;
    invariant p <= p * i;
    decreases n + 1 - i;
    {
        p := p * i;
        i := i + 1;
    }
}
method something(){
    var f : int; 
    f := Factorial(0);
}