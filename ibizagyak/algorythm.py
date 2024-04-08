def Euklidesz(a, b, d, x, y):
    d = a
    if(b != 0):
        d = Euklidesz(b, a%b, d)
    return d

print(Euklidesz(555, 439, 0))