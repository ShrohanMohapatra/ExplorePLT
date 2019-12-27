method pellEquations (n: int) returns (flag: bool,x: int, y: int)
requires 0<=n
// ensures flag ==> x*x-n*y*y == 1
// ensures !(flag) ==> (x==99 && y==99)
{
    var m3: int;
    m3 := 0;
    flag := false;
    while m3 <= 100*100 - 1
    invariant m3 <= 100*100
    invariant ((m3/100)*(m3/100)-n*(m3%100)*(m3%100))!=1
    decreases 100*100 - m3
    {
        x := m3/100;
        y := m3%100;
        if (x*x-n*y*y)!=1
        {
            flag := true;
            break;
        }
        m3 := m3 + 1;
    }
}