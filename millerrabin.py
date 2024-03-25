import gyorshatvany as gyh

def mr(p, a):
    d, S = p-1, 0
    while d%2 == 0:
        S+=1
        d = d/2
    if(gyh.gyors(a, d, p)==1):
        return True
    for r in range(S):
        if(gyh.gyors(a,d*(2**r), p) == p-1):
            return True
    return False

print(mr(561, 2)) 