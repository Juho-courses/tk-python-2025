sana = input("kirjoita sana: ")

vika = sana[-1].lower()

if vika == "a":
    print("viimeisenä aakkosten ensimmäinen kirjain")
elif vika == "ö":
    print("viimeisenä aakkosten viimeinen kirjain!")
else:
    print(f"sanasi loppuu kirjaimeen '{vika}'")
