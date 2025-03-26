sanat = []

sanat.append(input("kirjoita sana: "))
sanat.append(input("kirjoita toinen sana: "))
sanat.append(input("kirjoita kolmas sana: "))
sanat.append(input("ja vielä viimeinen sana: "))

if "koira" in sanat:
    print(f"koira löydetty {len(sanat)} sanan joukosta")
else:
    print(f"{len(sanat)} sanaa ja yksikään niistä ei ole koira")
