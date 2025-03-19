# Tee lista, johon tallennat arvoja. Suodata listasta duplikaatit pois.
# [1,2,2,3] → [1,2,3]

lista = [1,2,2,3]

lista = list(set(lista))
print(lista)

