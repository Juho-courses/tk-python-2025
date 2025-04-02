def kysele(maara):
    luvut = []

    while len(luvut) < maara:
        luku = int(input("luku: "))
        luvut.append(luku)

    return luvut


def prosessoi(luvut):
    pituus = len(luvut)
    summa = sum(luvut)
    avg = summa / pituus
    return (summa, pituus, avg)


def aloita():
    maara = int(input("montako lukua syötät: "))

    luvut = kysele(maara)

    tulokset = prosessoi(luvut)

    print(f"sum: {tulokset[0]}, len: {tulokset[1]}, avg: {tulokset[2]}")


aloita()
