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