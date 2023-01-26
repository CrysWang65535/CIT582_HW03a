import random

from params import p
from params import g


def keygen():
    sk = 0  # a
    pk = 0  # pow(g, a, p)
    q = (p - 1) / 2
    sk = random.SystemRandom().randint(1, q)
    pk = pow(g, sk, p)
    return pk, sk


def encrypt(pk, m):
    c1 = 0
    c2 = 0
    q = (p - 1) / 2
    r = random.SystemRandom().randint(1, q)
    c1 = pow(g, r, p)
    c2 = pow(pk, r, p) * pow(m, 1, p) % p
    return [c1, c2]


def decrypt(sk, c):
    m = 0
    c2 = c[1]
    c1 = c[0]
    m = pow(c2, 1, p) / pow(c1, sk, p)
    return m
