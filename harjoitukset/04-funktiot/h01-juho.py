def kysele_ja_palauta():
    d = dict()

    while True:
        avain = input('avain ("stop" lopettaa): ')
        if avain == "stop":
            break
        arvo = input("arvo: ")
        d[avain] = arvo

    return d


parit = kysele_ja_palauta()
print(parit)
