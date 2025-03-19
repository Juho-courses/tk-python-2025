# Käyttäen yhtä inputia, pyydä käyttäjältä pilkulla eroteltuna kokonaislukuja. Hajoita syöte tupleen omiksi arvoiksi ja tulosta syötettyjen arvojen lukumäärä.
# “1,2,3” → 3

syote = input('anna lukuja pilkulla eroteltuna: ')

hajoitus = tuple(syote.split(','))
maara = len(hajoitus)
print(f"määrä: {maara}")

# one-linerina
print(f"määrä: {len(tuple(syote.split(',')))}")


# lukukelvoton onelineri
# print(f"määrä: {len(tuple(input('anna lukuja pilkulla eroteltuna: ').split(',')))}")

