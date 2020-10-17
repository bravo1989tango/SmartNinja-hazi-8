hangulat = input("Szia! Milyen a hangulatod ma?\n").capitalize()

if hangulat == ("Boldog") or ("Szuper") or ("Jó") or ("Remek"):
    print("Örülök, hogy jól vagy! :)")
elif hangulat == ("Ideges"):
    print("Nyugi, vegyél 3 mély levegőt és lassan fújd ki. :O -> :°")
elif hangulat == ("Szomorú"):
    print("Fel a fejjel, lesz ez még rosszabb is! xD")
elif hangulat == ("Izgatott"):
    print("Na végre valami történt veled! :D")
elif hangulat == ("Nyugodt"):
    print("Emlékezz erre a pillanatra, mikor ideges vagy! :)")
else:
    print("Nem tudom értelmezni a hangulatod.")