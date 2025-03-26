i = input("Anna sana: ")

match i[-1]:
    case 'a':
        print("Viimeisenä aakkosten ensimmäinen kirjain!")
    case 'ö':
        print("Viimeisenä aakkosten viimeinen kirjain!")
    case _:
        print("Sanasi loppuu kirjaimeen " + i[-1])


    
