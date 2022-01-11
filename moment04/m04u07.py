förstatal=int(input("säg ditt första tal "))
avslutandetal=int(input("säg talet som loopen ska avslutas med "))
tal=int(input("säg ett tal "))
avbryttal=int(input("säg ett tal som ska bryta loop "))


nummer=förstatal -1 
while nummer < avslutandetal:
    nummer += 1


    if nummer == avbryttal:
        break


    if nummer == tal:
        continue

print(nummer)
