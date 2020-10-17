plusz = "+"
minusz = "-"
osztas = "/"
szorzas = "*"

while True:
    try:
        num1 = int(input("Kérem az első számot: "))
        num2 = int(input("Kérem a második számot: "))
    except ValueError:
        print("Számokat kérek!")
        continue
    muvelet = input("Kérem a műveletet: ")
    if muvelet == plusz:
        print("Az összeadás eredménye: " + str(num1 + num2))
        break
    elif muvelet == minusz:
        print("A kivonás eredménye: " + str(num1 - num2))
        break
    elif muvelet == osztas:
        print("Az osztás eredménye: " + str(num1 / num2))
        break
    elif muvelet == szorzas:
        print("A szorzás eredménye: " + str(num1 * num2))
        break
    else:
        print("Érvénytelen operátor!")
