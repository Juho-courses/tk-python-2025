# Kirjoita funktio, joka kysyy käyttäjältä avain-arvo pareja niin kauan, kunnes
# avain on 'stop' (tällöin ei enää kysytä arvoa). Funktio palauttaa käyttäjän
# syöttämät parit dictinä.

def ask_key_values():
    print("Syötä avain-arvo pareja välilyönnillä erotettuna.")
    print("Stop lopettaa")
    res = {}
    while True:
        a = input("Avain arvo: ")
        if a.lower() == "stop":
            return res
        k, v = a.split()
        res[k] = v

if __name__ == "__main__":
    r = ask_key_values()
    print(r)
