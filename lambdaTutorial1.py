y = lambda x: x
print(y(5))
z = lambda x: x+1
print(z(20))
t1 = lambda first,last: first[0].upper()
t2 = lambda first,last: t1(first,last)+''.join(first[i] for i in range(1,len(first)))
t3 = lambda first,last: t2(first,last)+' '+last[0].upper()
full_name = lambda first,last: t3(first,last)+''.join(last[i] for i in range(1,len(last)))
print(full_name('shrohan','mohapatra'))