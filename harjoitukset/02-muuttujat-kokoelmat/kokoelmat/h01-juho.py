# Luo lista, johon tallennat neljä arvoa. Tulosta listan toinen ja neljäs jäsen.
# Jatko: Tulosta toinen ja neljäs jäsen samalle riville, pilkulla eroteltuna

lista = [1,2,3,4]

print(lista[1], lista[3])

# jatko
print(lista[1], lista[3], sep=",")

# tai
print(str(lista[1]) + ", " + str(lista[3]))
