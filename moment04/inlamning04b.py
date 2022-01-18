def kvadratspel():
    sida1=int(input('välj ett första tal upp till tio.'))

    sida2=int(input('Välj ett andra tal upp till tio.'))

    area=sida1*sida2



    if sida1 == sida2:
        print('båda sidorna är lika långa, därför är det en kvadrat.')

    print("Höjden | Volymen")
    print("----------------")
    for x in range(1,11):
        print("   {}    | {} ".format(x, x*area))
    
    köraigen=input("Vill du göra en beräkning till (ja/nej)?")
    while köraigen == "ja":
        kvadratspel()
    if köraigen == "nej": 
        print("kod avslutad")

    

kvadratspel()
#fixa så att den faktiskt avbtryts