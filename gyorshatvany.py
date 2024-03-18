def gyors(alap, exp, mod):
    alap = alap % mod
    if(exp == 0): 
        return 0
    elif(exp == 1):
        return alap
    elif (exp%2==0):
        return gyors(alap*alap%mod, exp/2, mod)
    else:
        alap = alap * gyors(alap,exp-1, mod)%mod
    return alap
print(gyors(7,92,24))