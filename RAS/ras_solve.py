# %%
from Crypto.Util.number import *
import math
import numpy as np


def genparam(nbit):
    while True:
        a, b = getRandomRange(2, nbit), getRandomRange(32, nbit)
        if (a ** b).bit_length() == nbit:
            return a ** b


def genkey(nbit):
    p, q = [_ + (_ % 2) for _ in [genparam(nbit) for _ in '01']]
    while True:
        P = p + getPrime(31)
        if isPrime(P):
            while True:
                Q = q + getPrime(37)
                if isPrime(Q):
                    return P, Q


# %% find all genparam(512)

all_params = []

for a in range(2, 512):
    for b in range(32, 512):
        if (a ** b).bit_length() == 512:
            all_params.append((0, a, b, a**b))

print(len(all_params))
# %%


def SieveOfEratosthenes(n):
    n_s = math.floor(n**0.5)
    prime = np.ones(n+1, dtype=bool)

    for p in range(2, n_s+1):
        if (prime[p]):
            prime[p*p:n+1:p] = False

    return prime


prime_array = SieveOfEratosthenes(2**31)
print("Total prime numbers in range:", np.sum(prime_array))
prime_numbers_31bit = np.where(prime_array[2**30:])[0] + 2**30
print("Total prime numbers in my range:", len(prime_numbers_31bit))
print('Example', prime_numbers_31bit[0], isPrime(
    int(prime_numbers_31bit[0])), int(prime_numbers_31bit[0]).bit_length())
del prime_array
# %%
pubkey = 56469405750402193641449232753975279624388972985036568323092258873756801156079913882719631252209538683205353844069168609565141017503581101845476197667784484712057287713526027533597905495298848547839093455328128973319016710733533781180094847568951833393705432945294907000234880317134952746221201465210828955449

volunteer_pq_s = []
ram_const = 1  # 2
p_param_i = 1
for p_param in all_params:
    p_param = p_param[3]
    print(p_param_i, p_param)
    p_param_i += 1
    p_param += p_param % 2

    partition_len = len(prime_numbers_31bit)//ram_const
    for partition_i in range(ram_const+1):
        partitioned_P_s = prime_numbers_31bit[partition_i *
                                              partition_len:(partition_i+1)*partition_len] + p_param
        valid_partitioned_P_s = partitioned_P_s[np.array(
            pubkey) % partitioned_P_s == 0]

        for valid_P in valid_partitioned_P_s:
            volunteer_pq_s.append((valid_P, pubkey//valid_P))
            print((valid_P, pubkey//valid_P))

        del valid_partitioned_P_s
        print('  ', partition_i, len(volunteer_pq_s))

# %%
volunteer_p, volunteer_q = (7503181809956767523746965523445045476257163607925774521504848419053281285592652527357937939189782711610752940844746826826913644756871296753402980129494103, 7526061233844414054658272333288124411685335071877284335907504995816228844305448573362353388854643200579154642450347983868657774168720289858354259165638383)
e = 0x10001
n = volunteer_p * volunteer_q
d = inverse(e, (volunteer_p - 1) * (volunteer_q - 1))

c = 11104433528952071860984483920122173351342473018268740572598132083816861855404615534742178674185812745207876206939230069251889172817480784782618716608299615251541018034321389516732611030641383571306414414804563863131355221859432899624060128497648444189432635603082478662202695641001726208833663163000227827283

m = pow(c, d, n)

print(long_to_bytes(m).decode())