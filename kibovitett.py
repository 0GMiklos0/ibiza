def kea(a,b,lx = [0,1], ly = [1,0]):
    s = 1
    while(b != 0):
        r = a%b
        q = a//b
        resultx = r*q*lx[1]+lx[0]
        resulty = r * q * ly[1] + ly[0]
        a = b
        b = r
        (lx[0], lx[1]) = (lx[1], resultx)
        (ly[0], ly[1]) = (ly[1], resulty)
        s *= -1
    x = s * lx[0]
    y = -s * ly[0]
    (d,x,y) = (a,x,y)
    return (d,x,y)

print(kea(15,4,1))