def bovitett_eu(a, b, d, ly = [0, 1], lx = [1,0]):
    s = 1
    while(b != 0):
        r = a % b
        q = a//b
        a = b
        b = r
        x = lx[1]
        y = ly[1]
        print(x, y, end = " ")
        lx[1] = x*q+lx[0]
        ly[1] = y*q+ly[0]
        lx[0] = q * x
        ly[0] = q * y
        print(lx,ly, end = "\n")
        s *= -1
    x = s * lx[-2]
    y = -s * ly[-2]
    (d,x,y) = (a,x,y)
    return (d,x,y)

[print(i, end = "\n") for i in bovitett_eu(57,412, 1)]