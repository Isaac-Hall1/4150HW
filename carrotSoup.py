import sys
sys.setrecursionlimit(20000)

#inputs
n = int(input())
x = int(input())
y = int(input())

"""
SplitMultiply(x, y, n):
if n = 1
return x · y
else
m ← [n/2]
a ← [x/10^m]; b ← x mod 10m 〈〈x = 10^m*a + b〉〉
c ← [y/10^m]; d ← y mod 10m 〈〈 y = 10^m*c + d〉〉
e ← SplitMultiply(a,c, m)
f ← SplitMultiply(b, d, m)
g ← SplitMultiply(b,c, m)
h ← SplitMultiply(a, d, m)
return 10^2m*e + 10^m*(g + h) + f
"""

def splitmult(n,x,y:int) -> int:

    if n == 1:
        return x*y
    else:
        m = n//2
        a = x//(10**m)
        b = x % (10**m)
        c = y//(10**m)
        d = y % (10**m)
        e = splitmult(m,a,c)
        f = splitmult(m,b,d)
        g = splitmult(m,b,c)
        h = splitmult(m,a,d)
    
        return ((10**(2*m))*e+(10**m)*(g+h)+f)

def fastmult(n,x,y:int) -> int:
    if n == 1:
        return x*y
    else:
        m = n//2
        a = x//(10**m)
        b = x % (10**m)
        c = y//(10**m)
        d = y % (10**m)
        e = fastmult(m,a,c)
        f = fastmult(m,b,d)
        g = fastmult(m,a-b,c-d)
        return ((10**(2*m))*e+(10**m)*(e+f-g)+f)

print(fastmult(n,x,y))