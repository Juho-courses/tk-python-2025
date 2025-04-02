# Kirjoita ohjelma, joka ensin kysyy käyttäjältä montako lukua tämä aikoo
# syöttää. Tämän jälkeen ohjelma pyytää käyttäjältä halutun määrän lukuja.
# Syötetyt luvut käsitellään ja niistä lasketaan summa, lukumäärä ja keskiarvo.
# Tekninen toteutus jää muuten kehittäjän päätettäväksi, mutta lukujen kysely
# ja arvojen prosessointi pitää toteuttaa omissa funktioissaan. Prosessoinnin
# tekevä funktio palauttaa arvot tuplena. Kerro käyttäjälle prosessoinnin
# tulokset.
#
#     Esim. 3 → 1,2,3 → sum: 6, len: 3, avg: 2.0

# Esimerkki itse määritellystä poikkeuksesta
# Poikkeukset perii Exception luokan ja konstruktorissa kutsutaan perityn 
# luokan konstruktoria.
class NotANumberException(Exception):
    # Poikkeuksilla tulisi aina olla message attribuutti.
    # Muitakin attribuutteja voi olla, esimerkiksi 'id_number'
    def __init__(self, msg):
        super().__init__(msg)  # Kutsutaan perityn luokan konstruktoria ja 
                               # annetaan sille haluttu viesti

        self.message = msg     # Talletetaan viesti myös meidän omaan luokkaan.
                               # Tämä ei ole täysin välttämätöntä, mutta 
                               # helpottaa viestin esiin saamista virheestä.

def ask_count():
    while True:
        try:
            return int(input("Montako arvoa meinaat syöttää? "))
        except ValueError:
            # Otetaan kiinni ValueError ja nostetaan ihmisen helpommin 
            # tulkattava NotANumberException
            raise NotANumberException("Et syöttänyt numeroa ask_countissa..")


def form_list(l) -> list:
    result = []
    for i in range(l):
        try:
            n = int(input(f"Arvo {i}: "))
            result.append(n)
        except ValueError:
            raise NotANumberException("Et syöttänyt numeroa form_listissä..")

    return result

# Koska funktion nimi ei selitä itseään täysin auki, niin lisäsin docstringin.
def calculate_stats(l) -> tuple:
    """Calculates sum, length, and average of a list of numbers

    Returns:
        tuple: sum, length, average

    """
    s = sum(l)
    length = len(l)
    average = s / length
    return (s, length, average)


if __name__ == "__main__":
    try:
        n = ask_count()
        new_list = form_list(n)
        s, l, a = calculate_stats(new_list)
        print(f"Summa: {s}")
        print(f"Pituus: {l}")
        print(f"Keskiarvo: {a}")
    except NotANumberException as e:
        # Kun virheellä on message attribuutti, niin sitä pidetään 
        # automaattisesti virheen string muotoisena esityksenä.
        # Printin voisi tehdä myös tyyliin:
        # print(e.message)
        print(e)



