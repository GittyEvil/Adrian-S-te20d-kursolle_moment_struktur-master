def kvadratspel():
    sida1= input('välj ett första tal upp till tio.')

    sida2= input('Välj ett andra tal upp till tio.')

    if sida1.isnumeric() == False or sida1.isnumeric() == False:
        print("det är ingen siffra, försök igen.")
        kvadratspel()
    sida1 = int(sida1)
    sida2 = int(sida2)

    if sida1 < 0:
        sida1 == 1

    if sida1 > 10:
        sida1 == 10

    area = sida1 * sida2
    print(area)

    if sida1 == sida2:
        print('båda sidorna är lika långa, därför är det en kvadrat.')

    print("Höjden | Volymen")
    print("----------------")
    for x in range(1,11):
        print("  {}    |   {} ".format(x, area))

    köraigen=input("Vill du göra en beräkning till (ja/nej)?")

    if köraigen == "ja":
        kvadratspel()

    if köraigen == "nej":
        print("kod avslutad")



kvadratspel()
