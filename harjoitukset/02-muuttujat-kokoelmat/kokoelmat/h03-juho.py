# Käyttäen yhtä inputia, pyydä käyttäjältä pilkulla eroteltuna kokonaislukuja. Hajoita syöte listaan omiksi arvoiksi ja tulosta lista siten, että sen ovat jäsenet käänteisessä järjestyksessä.
# “1,2,3” → [’3’, ‘2’, ‘1’]

syote = input('anna lukuja pilkulla eroteltuina: ')

syote = syote.split(',')[::-1]

print(syote)
