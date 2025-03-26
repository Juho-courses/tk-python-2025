x = input("Anna sanoja välilyönnillä eroteltuna: ").split(" ")

if "koira" in x:
    print(f"Koira löydetty {len(x)} sanan joukosta.")
else:
    print(f"{len(x)} sanaa ja yksikään niistä ei ole koira :(")
