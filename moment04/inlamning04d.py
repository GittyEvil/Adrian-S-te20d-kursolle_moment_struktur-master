
#skapar en funktion
def kvadratspel():
    lagrainfo  = []

    #frågar användaren om två tal från 1-10 och höjd
    sida1= input('välj ett första tal upp till tio.')

    sida2= input('Välj ett andra tal upp till tio.')

    höjd = input("väl en siffra upp till tio för höjd")

    #lägger till svaren i en lista
    lagrainfo.append(sida1)
    lagrainfo.append(sida2)
    lagrainfo.append(höjd)
    print(lagrainfo)

    #ifall talet inte är ett nummer kommer man få välja nya tal
    if sida1.isnumeric() == False or sida1.isnumeric() == False:
        print("det är ingen siffra, försök igen.")
        kvadratspel()

    sida1 = int(sida1)
    sida2 = int(sida2)

    if sida1 < 0:
        sida1 == 1

    if sida1 > 10:
        sida1 == 10

    #räknar snabbt ut arean
    area = sida1 * sida2

    print(area)
    #ifall båda sidor är lika långa printas det ut.
    if sida1 == sida2:
        print('båda sidorna är lika långa, därför är det en kvadrat.')

    print("Höjden | Volymen")
    print("----------------")
    #loopar ut hur det ska se ut med 1-10 med | i mitten
    for x in range(1,11):
        print("  {}    |   {} ".format(x, area))

    #frågar användaren om hen vill köra igen, skapade funktionen för att lätt kunna börja om med hela "spelet"
    köraigen=input("Vill du göra en beräkning till (ja/nej)?")
    
    if köraigen == "ja":
        kvadratspel()

    if köraigen == "nej":
        print("kod avslutad")


#för att starta "spelet/programmet"
kvadratspel()


