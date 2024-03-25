import gyorshatvany
import kibovitett

def kinai(p,q,c,d):
    c1 = gyorshatvany.gyors(c%p,d%(p-1),p)
    c2 = gyorshatvany.gyors(c%p,d%(q-1),q)
    (y1, y2) = kibovitett.kea(q,p)
    #lnko, y1, y2 = kea(q, p)
    m = (c1 * y1 * q + c2 * y2 * p) % p*q
    while m <= 0:
        m += p * q
    return m