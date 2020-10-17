

rejtett_szam = 67

#IF-ELSE
#tipp = int(input("Kérem a tippet: "))
#if tipp == rejtett_szam:
#    print("Mekkora mázlid van! Eltaláltad a számot!")
#else:
#    print("Ez most nem jött össze! Próbáld újra.")

#WHILE LOOP
while True:
    try:
        tipp = int(input("Kérem a tippet: "))
    except ValueError:
        print("Adjon meg egy számot!")
        continue
    else:
        if tipp == rejtett_szam:
            print("Eltaláltad!")
            break
        else:
            continue