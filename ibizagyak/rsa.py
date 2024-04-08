from chinese_rem import chinese_rem
import random
from miller_rabin import is_prime_mr
from modular_exp import modular_exp
from eucledian import ext_euclid
from gyorshatvany import gyors

def keygen():
    p, q = [random.randint(100,100000) for i in range(2)]
    while(not(is_prime_mr(q) and is_prime_mr(p) and p == q)):
        p, q = [random.randint(100,100000) for i in range(2)]
    n = p * q
    phin = (p-1)*(q-1)
    e = random.randint % phin + 1
    lkno, x, d = ext_euclid(phin, e)
    return (p,q,n,phin,e,d)

def enc(m, e, n):
    message = gyors(m, e, n)
    return message

def dec(m,d, p, q, n):
    message = chinese_rem(m, d, p, q, n)
    return message

def main():
    p,q,n,phin,e,d = keygen()
    message = input("Message:")
    message = enc(message, e, n)
    print(message)
    message = dec(d,p,q,n)
    print(message)