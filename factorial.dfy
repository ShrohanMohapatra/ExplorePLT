function fact (n:nat) : nat
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