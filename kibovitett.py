def kea(a,b,d):
    s = 1
    lx = [0,1]
    ly = [1,0]
    while(b != 0):
        r = a%b
        q = a//b
        a = b
        b = r
        resultx = q * lx[1] + lx[0]
        resulty = q * ly[1] + ly[0]
        print(resultx, resulty)
        (lx[0], lx[1]) = (lx[1], resultx)
        (ly[0], ly[1]) = (ly[1], resulty)
        s *= -1
    x = s * lx[0]
    y = -s * ly[0]
    (d,x,y) = (a,x,y)
    return (d,x,y)

print(kea(15,4,1))