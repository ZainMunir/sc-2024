def pretty_print(dictionary):
    for key in dictionary:
        # print rounded
        print(key, round(dictionary[key], 3))


test = False
if test:
    M = {
        "a": 1 / 4,
        "b": 3 / 10,
        "c": 3 / 20,
        "d": 3 / 10,
    }
    K = {
        "k1": 1 / 4,
        "k2": 1 / 2,
        "k3": 1 / 4,
    }
    encryption_sceme = {
        ("a", "k1"): 3,
        ("a", "k2"): 3,
        ("a", "k3"): 4,
        ("b", "k1"): 4,
        ("b", "k2"): 1,
        ("b", "k3"): 3,
        ("c", "k1"): 2,
        ("c", "k2"): 4,
        ("c", "k3"): 1,
        ("d", "k1"): 1,
        ("d", "k2"): 2,
        ("d", "k3"): 2,
    }
else:
    M = {
        "a": 1 / 3,
        "b": 4 / 15,
        "c": 1 / 5,
        "d": 1 / 5,
    }
    K = {
        "k1": 1 / 5,
        "k2": 3 / 10,
        "k3": 1 / 5,
        "k4": 3 / 10,
    }
    encryption_sceme = {
        ("a", "k1"): 3,
        ("a", "k2"): 2,
        ("a", "k3"): 4,
        ("a", "k4"): 1,
        ("b", "k1"): 1,
        ("b", "k2"): 4,
        ("b", "k3"): 2,
        ("b", "k4"): 3,
        ("c", "k1"): 4,
        ("c", "k2"): 1,
        ("c", "k3"): 3,
        ("c", "k4"): 2,
        ("d", "k1"): 2,
        ("d", "k2"): 3,
        ("d", "k3"): 1,
        ("d", "k4"): 4,
    }

C = {
    1: 0,
    2: 0,
    3: 0,
    4: 0,
}

for key in encryption_sceme:
    C[encryption_sceme[key]] += M[key[0]] * K[key[1]]


def cipher_given_plain(cipher, plain):
    return sum([K[key] for key in K if encryption_sceme[(plain, key)] == cipher])


def plain_given_cipher(plain, cipher, ciphers_given_plains):
    return (M[plain] * ciphers_given_plains[(cipher, plain)]) / C[cipher]


ciphers_given_plains = {}
for p in M:
    for c in C:
        ciphers_given_plains[(c, p)] = cipher_given_plain(c, p)

plains_given_ciphers = {}
for c in C:
    for p in M:
        plains_given_ciphers[(p, c)] = plain_given_cipher(p, c, ciphers_given_plains)


print("p(P=m)")
pretty_print(M)
print()
print("p(K=k)")
pretty_print(K)
print()
print("p(C=c)")
pretty_print(C)
print()
print("p(C=c|P=m)")
pretty_print(ciphers_given_plains)
print()
print("p(P=m|C=c)")
pretty_print(plains_given_ciphers)
